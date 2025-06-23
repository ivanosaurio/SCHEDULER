import flet as ft
from datetime import datetime
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from components.sidebar import Sidebar
from components.composer import PostComposer
from components.placeholder import PlaceholderView
from services.supabase_service import fetch_posts, add_post, delete_post, update_post
from components.queue_item import QueueItem

class DashboardView(ft.Row):
    def __init__(self, page: ft.Page, user_id: str, on_logout):
        super().__init__()
        #Fila principal
        self.page_ref = page
        self.expand = True
        self.vertical_alignment = ft.CrossAxisAlignment.STRETCH
        
        #Sesion de Usuario
        self.user_id = user_id
        self.on_logout = on_logout
        print(f"[DashoardView] Inicializado para el usuario: {self.user_id}")
        
        #Componentes
        self.queue_list_view = ft.Column(
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE
        )
        
        self.post_composer = PostComposer(on_schedule_click=self.handle_schedule_click)
        self.sidebar = Sidebar(self.change_view, on_logout_click=self.on_logout)
        
        page.overlay.extend([
            self.post_composer.date_picker,
            self.post_composer.time_picker,
            self.post_composer.file_picker
        ])
        
        self.views = {
            "Cola": self.create_queue_view(),
            "Analíticas": self.create_analytics_view(),
            "Configuración": self.create_settings_view()
        }
        
        self.main_content = ft.Container(
            expand=True,
            padding=40,
            content= self.views["Cola"]
        )
        
        self.controls = [
            self.sidebar,
            self.main_content
        ]
        self.page_ref.run_task(self.load_queue_posts)
    
    def open_edit_dialog(self, post_data: dict):
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
        result = update_post(post_id, new_content, new_scheduled_at)
        
        if result.get("success"):
            self.post_composer.show_feedback("¡Publicación actualizada con éxito!")
            
            await self.load_queue_posts()
        else:
            error_message  = result.get('error', 'Ocurrió un error desconocido.')
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
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
        result = delete_post(post_id)
        
        if result["success"]:
            self.post_composer.show_feedback("Publicación eliminada correctamente.")
            await self.load_queue_posts()
        else:
            error_msg = result.get('error', 'Error desconocido al eliminar.')
            self.post_composer.show_feedback(f"Error: {error_msg}", is_error=True)
    
    def handle_schedule_click(self, content: str, scheduled_at: datetime | None, image_url: str | None):
        self.page_ref.run_task(self._do_schedule_and_reload, content, scheduled_at, image_url)
    
    async def _do_schedule_and_reload(self, content: str, scheduled_at: datetime | None, image_url: str | None):
        if not content or not content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        
        result = add_post(self.user_id, content, scheduled_at, image_url)
        
        if result.get("success"):
            self.post_composer.clear()
            self.post_composer.show_feedback("¡Publicación programada con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
    async def confirm_edit(self, post_id: str, new_content: str, new_scheduled_at: datetime):
        print(f"Intentando actualizar post {post_id} con nuevo contenido: '{new_content}'")
        
        if not new_content or not new_content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        
        result = update_post(post_id, new_content, new_scheduled_at)
        
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
        
        result = fetch_posts(self.user_id)
        self.queue_list_view.controls.clear()
        
        # 3. Procesar el resultado
        if result["success"]:
            posts = result["data"]
            if not posts:
                # Caso: éxito, pero no hay posts
                self.queue_list_view.controls.append(
                    ft.Container(
                        padding=20,
                        content=ft.Text("Tu cola está vacía.",color=TEXT_SECONDARY)
                    )
                )
            else:
                # Caso: éxito y hay posts
                print(f"[DashboardView] Iniciando bucle para crear {len(posts)} items.")
                for post in posts:
                    item = QueueItem(
                        post_data=post,
                        on_edit_click=self.open_edit_dialog,
                        on_delete_click=self.open_delete_dialog
                        )
                    
                    item.delete_button.data = post.get("id")
                    print(f"    -> Asignando on_click para post {post.get('id')}.")
                    print(f"       ¿Existe self.open_delete_dialog? {hasattr(self, 'open_delete_dialog')}")
                    print(f"       Tipo de self.open_delete_dialog: {type(self.open_delete_dialog)}")
                    item.delete_button.on_click = self.open_delete_dialog
                    
                    self.queue_list_view.controls.append(item)
        else:
            # Caso: error
            self.queue_list_view.controls = [ft.Text(f"Error: {result['error']}", color=ft.Colors.RED_500)]
        if self.page_ref and self.page_ref.controls:
            self.page_ref.update()
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
    
    def create_settings_view(self):
        return PlaceholderView(
            icon_name=ft.Icons.SETTINGS,
            title="Configuración",
            message="Aquí podrás gestionar tus cuentas sociales conectadas, las preferencias de la aplicación y los detalles detu perfil."
        )
    
    def change_view(self, view_name: str):
        self.main_content.content = self.views.get(view_name)
        self.main_content.update()