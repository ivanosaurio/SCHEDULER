import flet as ft
from datetime import datetime
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from components.sidebar import Sidebar
from components.composer import PostComposer
from services.supabase_service import fetch_posts, add_post, delete_post, update_post
from components.queue_item import QueueItem

class DashboardView(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        #Fila principal
        self.page_ref = page
        self.expand = True
        self.vertical_alignment = ft.CrossAxisAlignment.STRETCH
        
        #Componentes
        
        self.queue_list_view = ft.Column(
            spacing=10,
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE
        )
        
        self.post_composer = PostComposer(on_schedule_click=self.handle_schedule_click)
        self.sidebar = Sidebar(self.change_view)
        
        page.overlay.append(self.post_composer.date_picker)
        page.overlay.append(self.post_composer.time_picker)
        
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
    
    def open_delete_dialog(self, e):
        print("[DashboardView] open_delete_dialog FUE LLAMADO!")
        post_id = e.control.data
        
        def handle_confirm(dlg_ref):
            self.page_ref.run_task(self.confirm_delete, post_id, dlg_ref)
        
        def handle_cancel(dlg_ref):
            self.page_ref.close(dlg_ref)
            self.page_ref.update()
        
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
    
    async def confirm_delete(self, post_id: str, dlg: ft.AlertDialog):
        print(f"Confirmada la eliminación del post: {post_id}")
        
        self.page_ref.close(dlg)
        self.page_ref.update(
            
        )
        result = delete_post(post_id)
        
        if result["success"]:
            print(f"Post {post_id} eliminado con éxito de la base de datos.")
            self.post_composer.show_feedback("Publicación eliminada correctamente.")
            await self.load_queue_posts()
        else:
            error_msg = result.get('error', 'Error desconocido al eliminar.')
            print(f"Fallo al eliminar el post: {error_msg}")
            self.post_composer.show_feedback(f"Error: {error_msg}", is_error=True)
        
    def handle_schedule_click(self, content: str, scheduled_at: datetime | None):
        self.page_ref.run_task(self._do_schedule_and_reload, content, scheduled_at)
    
    async def _do_schedule_and_reload(self, content: str, scheduled_at: datetime | None):
        if not content or not content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        
        result = add_post(content, scheduled_at)
        
        if result.get("success"):
            self.post_composer.clear()
            self.post_composer.show_feedback("¡Publicación programada con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
    def open_edit_dialog(self, post_data: dict):
        post_id = post_data.get("id")
        
        edit_textfield = ft.TextField(
            value=post_data.get("content"),
            multiline=True,
            min_lines=4,
            border=ft.InputBorder.UNDERLINE,
            hint_text="Edita tu publicación..."
        )
        
        def handle_confirm(e):
            self.page_ref.close(dlg)
            original_scheduled_at = datetime.fromisoformat(post_data.get("scheduled_at"))
            self.page_ref.run_task(
                self.confirm_edit,
                post_id,
                edit_textfield.value,
                original_scheduled_at
            )
        
        def handle_cancel(e):
            self.page_ref.close(dlg)
            self.page_ref.close(dlg)
        
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Publicación"),
            content=ft.Column(
                tight=True,
                controls=[
                    edit_textfield,
                    ft.Text(f"ID del Post: {post_id}", italic=True, size=10, color=TEXT_SECONDARY)
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
        self.page_ref.update()
        
        result = fetch_posts()
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
        return ft.Column(
            controls=[ft.Text("Vista de Analíticas", size=30, style=ft.TextStyle(color=TEXT_PRIMARY))]
        )
    
    def create_settings_view(self):
        return ft.Column(
            controls=[ft.Text("Vista de Configuracion", size=30, style=ft.TextStyle(color=TEXT_PRIMARY))])
    
    def change_view(self, view_name: str):
        self.main_content.content = self.views.get(view_name)
        self.main_content.update()