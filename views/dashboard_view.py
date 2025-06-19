import flet as ft
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from components.sidebar import Sidebar
from components.composer import PostComposer
from services.supabase_service import fetch_posts, add_post
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
    
    async def initialize(self):
        print("DashboardView.initialize() llamado. Cargando posts...")
        await self.load_queue_posts()
        
    async def handle_schedule_click(self, content: str):
        self.page_ref.run_task(self._do_schedule_and_reload, content)
    
    async def _do_schedule_and_reload(self, content: str):
        """
        Esta es la lógica ASÍNCRONA real. Se ejecuta en un contexto seguro
        proporcionado por page.run_task.
        """
        if not content or not content.strip():
            self.post_composer.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
            return
        
        result = add_post(content)
        
        if result.get("success"):
            self.post_composer.clear()
            self.post_composer.show_feedback("¡Publicación programada con éxito!")
            await self.load_queue_posts()
        else:
            error_message = result.get('error', 'Ocurrió un error desconocido.')
            self.post_composer.show_feedback(f"Error: {error_message}", is_error=True)
    
    async def load_queue_posts(self):
        # 1. Mostrar estado de carga
        print("--- Iniciando load_queue_posts ---")
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
                for post in posts:
                    self.queue_list_view.controls.append(QueueItem(post))
        else:
            # Caso: error
            self.queue_list_view.controls = [ft.Text(f"Error: {result['error']}", color=ft.Colors.RED_500)]
        self.page.update()
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