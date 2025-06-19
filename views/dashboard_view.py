import flet as ft
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from components.sidebar import Sidebar
from components.composer import PostComposer
from services.supabase_service import add_post

class DashboardView(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        #Fila principal
        self.page_ref = page
        self.expand = True
        self.vertical_alignment = ft.CrossAxisAlignment.STRETCH
        
        #Componentes
        self.post_composer = PostComposer(on_schedule_click=self.handle_schedule_click)
        self.sidebar = Sidebar(self.change_view)
        
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
    
    def create_queue_view(self):
        return ft.Column(
            expand=True,
            spacing=20,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                self.post_composer,
                ft.Text("Cola de Publicaciones", size=20, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                ft.Column(
                    
                )
            ]
        )
    
    def handle_schedule_click(self, content: str):
        if not content or not content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        print(f"Intentando guardar el post: '{content}'")
        result = add_post(content)
        
        if result.get("success"):
            print ("¡Éxito! El post se guardó en Supabase.")
            self.post_composer.show_feedback("¡Publicación programada con éxito!")
            self.post_composer.clear()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            print(f"Fallo al guardar. Error: {error_message}")
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
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