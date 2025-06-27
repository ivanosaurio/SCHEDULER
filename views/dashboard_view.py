import flet as ft
import threading, asyncio
from datetime import datetime
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from components.sidebar import Sidebar
from components.composer import PostComposer
from components.placeholder import PlaceholderView
from components.queue_item import QueueItem
from views.settings_view import SettingsView
from services import twitter_service, supabase_service

class DashboardView(ft.Row):
    def __init__(self, page: ft.Page, user_id: str, on_logout, on_connect_twitter):
        super().__init__()
        #Fila principal
        self.page_ref = page
        self.expand = True
        self.vertical_alignment = ft.CrossAxisAlignment.STRETCH
        
        #Sesion de Usuario
        self.user_id = user_id
        self.on_logout = on_logout
        self.on_connect_twitter = on_connect_twitter
        self.connected_accounts = []
        print(f"[DashoardView] Inicializado para el usuario: {self.user_id}")
        self.post_composer = PostComposer(
            on_schedule_click=self.handle_schedule_post_click,
            on_thread_schedule_click=self.handle_schedule_thread_click
        )
        #Feedback
        self.feedback_text = ft.Text(value="", color=TEXT_PRIMARY)
        self.feedback_container = ft.Container(
            content=self.feedback_text, # El texto va DENTRO del contenedor
            # Propiedades de caja que antes estaban mal puestas en ft.Text:
            padding=15,
            bgcolor=ft.Colors.with_opacity(0.9, SURFACE),
            border=ft.border.all(1, BORDER),
            border_radius=8,
            # Propiedades de posicionamiento y visibilidad:
            visible=False,
            bottom=20,
            right=20,
            animate_opacity=300, # Pequeño extra para una aparición/desaparición suave
        )
        self.feedback_timer = None
        
        #Componentes
        self.queue_list_view = ft.Column(
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE
        )
        self.sidebar = Sidebar(on_change=self.change_view, on_logout_click=self.on_logout)
        
        page.overlay.extend([
            self.post_composer.date_picker,
            self.post_composer.time_picker,
            self.post_composer.file_picker,
            self.feedback_container
        ])
        
        self.views = {
            "Cola": self.create_queue_view(),
            "Analíticas": self.create_analytics_view(),
            "Configuración": ft.Container(content=ft.ProgressRing())
        }
        
        self.main_content = ft.Container(
            expand=True,
            padding=40,
            content= self.views["Cola"]
        )
        
        self.controls = [
            self.sidebar,
            self.main_content,
        ]
        self.page_ref.run_task(self.load_initial_data)
    
    def handle_schedule_thread_click(self, scheduled_at: datetime, posts_content: list[str]):
        self.page_ref.run_task(self.do_schedule_thread_and_reload, scheduled_at, posts_content)
    
    async def do_schedule_thread_and_reload(self, scheduled_at: datetime, posts_content: list[str]):
        self.show_feedback("Programando hilo...", is_error=False)
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None,
            supabase_service.add_thread,
            self.user_id,
            "x", #plataforma harcodeada por ahora
            scheduled_at,
            posts_content
        )
        
        if result.get("success"):
            self.post_composer.clear()
            self.show_feedback("¡Hilo programado con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            self.show_feedback(f"Error: {error_message}", is_error=True)
    
    async def load_initial_data(self):
        
        await self.refresh_settings_data()
        await self.load_queue_posts()
        await self.change_view("Cola")
    
    async def refresh_settings_data(self):
        print("[DashboardView] Obteniendo datos de cuentas sociales...")
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, supabase_service.fetch_social_accounts, self.user_id)
        
        if result.get("success"):
            self.connected_accounts = result.get("data", [])
            if self.connected_accounts and hasattr(self, 'post_composer'):
                twitter_account = next((acc for acc in self.connected_accounts if acc.get("platform") == "x"), None)
                if twitter_account:
                    profile_url = twitter_account.get("profile_image_url")
                    self.post_composer.update_avatar(profile_url)
        else:
            self.connected_accounts = []
            self.show_feedback(f"Error al cargar cuentas: {result.get('error')}", is_error=True)
            self.post_composer.update_avatar(None)
    
    async def process_twitter_callback(self, result: dict):
        app_instance = self.page_ref.app_instance
        
        if not result.get("success"):
            self.show_feedback(f"Error de autenticacion: {result.get('error')}", is_error=True)
            return
        oauth_verifier = result.get("oauth_verifier")
        if not oauth_verifier or not app_instance.temp_oauth_handler:
            self.show_feedback("Error interno: no se pudo completar la autenticacion.", is_error=True)
            return
        self.show_feedback("Verificacion recibida. Obteniendo tokens finales...", is_error=False)
        
        loop = asyncio.get_running_loop()
        token_result = await loop.run_in_executor(
            None,
            twitter_service.get_twitter_access_token,
            app_instance.temp_oauth_handler,
            oauth_verifier
        )
        
        app_instance.temp_oauth_handler = None
        
        if not token_result.get("success"):
            self.show_feedback(f"Error al obtener token: {token_result.get('error')}", is_error=True)
            return
        username = token_result["username"]
        self.show_feedback(f"¡Tokens obtenidos para @{username}! Guardando...", is_error=False)
        
        save_result = await loop.run_in_executor(
            None,
            supabase_service.save_social_account,
            self.user_id,
            "x",
            username,
            token_result["access_token"],
            token_result["access_token_secret"],
            token_result["profile_image_url"]
        )
        
        if save_result.get("success"):
            self.show_feedback(f"¡Cuenta @{token_result['username']} conectada con exito!", is_error=False)
            if hasattr(self, 'post_composer'):
                self.post_composer.update_avatar(token_result.get("profile_image_url"))
            await self.refresh_settings_data()
            await self.sidebar.on_change("Configuración")
        else:
            self.show_feedback(f"Error al guardar: {save_result.get('error')}", is_error=True)
    
    def show_feedback(self, message: str, is_error: bool = False):
        print(f"[DashboardView] Mostrando feedback: '{message}'")
        
        # Actualizamos el texto y el color del control de texto INTERNO
        self.feedback_text.value = message
        self.feedback_text.color = ft.Colors.RED_400 if is_error else ft.Colors.GREEN_400
        
        # Hacemos visible el CONTENEDOR
        self.feedback_container.visible = True
        
        # Actualizamos solo el contenedor en la UI
        self.feedback_container.update()
        
        if self.feedback_timer:
            self.feedback_timer.cancel()
            
        self.feedback_timer = threading.Timer(4.0, self.hide_feedback)
        self.feedback_timer.start()
    
    def hide_feedback(self):
        self.feedback_container.visible = False
        if self.feedback_container.page:
            self.feedback_container.update()
    
    def open_edit_dialog(self, post_data: dict):
        if post_data.get("thread_id"):
            self.show_feedback("La edición de hilos completos estará disponible pronto.", is_error=True)
            return
        post_id = post_data.get("id")
        
        self.edit_selected_date = None
        self.edit_selected_time = None
        
        original_scheduled_at = datetime.fromisoformat(post_data.get("scheduled_at"))
        
        selected_date =None
        selected_time =None
        
        def handle_date_change(e):
            nonlocal selected_date
            selected_date = e.control.value
            self.page_ref.open(time_picker)
        
        def handle_time_change(e):
            nonlocal selected_time
            selected_time = e.control.value
            
            if selected_date and selected_time:
                final_datetime = datetime.combine(selected_date, selected_time)
                edit_scheduled_display.value = f"Nuevo horario: {final_datetime.strftime('%d de %B, %H:%M')}"
                edit_scheduled_display.visible = True
                dlg.update()
        
        date_picker = ft.DatePicker(
            on_change=handle_date_change,
            first_date=datetime.now(),
            help_text="Selecciona una nueva fecha"
        )
        
        time_picker = ft.TimePicker(
            on_change=handle_time_change,
            confirm_text="Confirmar",
            help_text="Selecciona una nueva hora"
        )
        
        self.page_ref.overlay.extend([date_picker, time_picker])
        
        edit_textfield = ft.TextField(
            value=post_data.get("content"),
            multiline=True,
            min_lines=4,
            border=ft.InputBorder.UNDERLINE
        )
        
        edit_scheduled_display = ft.Text(
            value=f"Programado para: {original_scheduled_at.strftime('%d de %B, %H:%M')}",
            color=TEXT_SECONDARY,
            italic=True
        )
        
        def handle_confirm(e):
            self.page_ref.close(dlg)
            
            new_scheduled_at = original_scheduled_at
            if selected_date and selected_time:
                new_scheduled_at = datetime.combine(selected_date, selected_time)
            
            self.page_ref.run_task(
                self.confirm_edit,
                post_id,
                edit_textfield.value,
                new_scheduled_at
            )
        
        def handle_cancel(e):
            self.page_ref.close(dlg)
        
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Publicación"),
            content=ft.Column(
                tight=True,
                controls=[
                    edit_textfield,
                    ft.Divider(height=10, color="transparent"),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            edit_scheduled_display,
                            ft.IconButton(
                                icon=ft.Icons.CALENDAR_MONTH,
                                on_click=lambda _: self.page_ref.open(date_picker),
                                tooltip="Cambiar fecha y hora"
                            )
                        ]
                    )
                ]
            ),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.TextButton("Cancelar", on_click=handle_cancel),
                ft.FilledButton("Guardar Cambios", on_click=handle_confirm)
            ]
        )
        
        self.page_ref.open(dlg)
        self.page_ref.update()
    
    async def confirm_edit(self, post_id: str, new_content: str, new_scheduled_at: datetime):
        print(f"Actualizando post {post_id} a las {new_scheduled_at.isoformat()}")
        
        if not new_content or not new_content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, supabase_service.update_post, post_id, new_content, new_scheduled_at)
        
        if result.get("success"):
            self.show_feedback("¡Publicación actualizada con éxito!")
            
            await self.load_queue_posts()
        else:
            error_message  = result.get('error', 'Ocurrió un error desconocido.')
            self.show_feedback(f"Error: {error_message}", is_error=True)
    
    def open_delete_dialog(self, e):
        print("[DashboardView] open_delete_dialog FUE LLAMADO!")
        post_id = e.control.data
        
        def handle_confirm(e_confirm):
            self.page_ref.close(dlg)
            self.page_ref.run_task(self.confirm_delete, post_id)
        
        def handle_cancel(e_cancel):
            self.page_ref.close(dlg)
        
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar Eliminación"),
            content=ft.Text("¿Estás seguro de que quieres eliminar este post?"),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: handle_cancel(dlg)),
                ft.FilledButton("Eliminar", on_click=lambda _: handle_confirm(dlg))
            ]
        )
        self.page_ref.open(dlg)
        self.page_ref.update()
    
    async def confirm_delete(self, post_id: str):
        print(f"Confirmada la eliminación del post: {post_id}")
        loop = asyncio.get_running_loop()
        result = loop.run_in_executor(None, supabase_service.delete_post, post_id)
        
        if result["success"]:
            self.post_composer.show_feedback("Publicación eliminada correctamente.")
            await self.load_queue_posts()
        else:
            error_msg = result.get('error', 'Error desconocido al eliminar.')
            self.post_composer.show_feedback(f"Error: {error_msg}", is_error=True)
    
    def handle_schedule_post_click(self, content: str, scheduled_at: datetime | None, image_url: str | None):
        self.page_ref.run_task(self._do_schedule_and_reload, content, scheduled_at, image_url)
    
    async def _do_schedule_and_reload(self, content: str, scheduled_at: datetime | None, image_url: str | None):
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None,
            supabase_service.add_post,
            self.user_id,
            content,
            scheduled_at,
            image_url
        )
        
        if result.get("success"):
            self.post_composer.clear()
            self.show_feedback("¡Publicación programada con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            self.show_feedback(f"Error: {error_message}", is_error=True)
    
    async def confirm_edit(self, post_id: str, new_content: str, new_scheduled_at: datetime):
        print(f"Intentando actualizar post {post_id} con nuevo contenido: '{new_content}'")
        
        if not new_content or not new_content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        
        result = supabase_service.update_post(post_id, new_content, new_scheduled_at)
        
        if result.get("success"):
            self.post_composer.show_feedback("¡Publicación actualizada con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido')
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
    async def load_queue_posts(self):
        # 1. Mostrar estado de carga
        print("--- Iniciando load_queue_posts ---")
        self.queue_list_view.controls.clear()
        self.queue_list_view.controls = [ft.Row([ft.ProgressRing(), ft.Text("Cargando publicaciones...")], alignment=ft.MainAxisAlignment.CENTER)]
        if self.page_ref.controls:
            self.update()
        
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None,
            supabase_service.fetch_posts, self.user_id
        )
        self.queue_list_view.controls.clear()
        
        if result["success"]:
            posts = result["data"]
            if not posts:
                self.queue_list_view.controls.append(
                    ft.Container(
                        padding=20,
                        content=ft.Text("Tu cola está vacía.",color=TEXT_SECONDARY)
                    )
                )
            else:
                print(f"[DashboardView] Iniciando bucle para crear {len(posts)} items.")
                for post in posts:
                    item = QueueItem(
                        post_data=post,
                        on_edit_click=self.open_edit_dialog,
                        on_delete_click=self.open_delete_dialog
                    )
                    self.queue_list_view.controls.append(item)
        else:
            self.queue_list_view.controls = [ft.Text(f"Error: {result['error']}", color=ft.Colors.RED_500)]
        if self.page_ref and self.page_ref.controls:
            self.update()
        print("--- Finalizado load_queue_posts ---")
    
    def create_queue_view(self):
        return ft.Column(
            expand=True,
            spacing=20,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                self.post_composer,
                ft.Text("Cola de Publicaciones", size=20, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                self.queue_list_view
            ]
        )
    
    def create_analytics_view(self):
        return PlaceholderView(
            icon_name=ft.Icons.INSIGHTS,
            title="Analíticas",
            message="Métricas, rendimiento de posts y seguimiento de tu crecimiento. ¡Esta función estará disponible próximamente!"
        )
    
    async def change_view(self, view_name: str):
        self.sidebar.set_activate(view_name)
        self.page_ref.overlay.clear()
        self.page_ref.overlay.append(self.feedback_container)
        self.main_content.content = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.ProgressRing()
            )
        self.main_content.update()
        
        if view_name == "Cola":
            self.main_content.content = self.create_queue_view()
            self.page_ref.overlay.extend([
                self.post_composer.date_picker,
                self.post_composer.time_picker,
                self.post_composer.file_picker
                ])
        elif view_name == "Configuración":
            await self.refresh_settings_data()
            self.main_content.content = SettingsView(
                on_connect_twitter=self.on_connect_twitter,
                connected_accounts=self.connected_accounts
            )
        elif view_name == "Analíticas":
            self.main_content.content = self.create_analytics_view()
        
        self.main_content.update()