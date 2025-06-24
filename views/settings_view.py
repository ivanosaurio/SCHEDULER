import flet as ft
from theme import TEXT_PRIMARY, TEXT_SECONDARY, BORDER

class SettingsView(ft.Column):
    def __init__(self, on_connect_twitter):
        super().__init__()
        self.on_connect_twitter = on_connect_twitter
        
        self.spacing = 20
        self.controls = [
            ft.Text(
                "Configuración",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=TEXT_PRIMARY
                ),
            ft.Text("Gestiona tus cuentas sociales y preferencias de la aplicación.", color=TEXT_SECONDARY),
            ft.Divider(),
            ft.Text(
                "Cuentas Conectadas",
                size=18, 
                width=ft.FontWeight.W_600,
                color=TEXT_PRIMARY
            ),
            ft.Container(
                padding=20, 
                border=ft.border.all(1, BORDER),
                border_radius=8,
                content=ft.Text("Aún no has conectado ninguna cuenta.", color=TEXT_SECONDARY)
            ),
            ft.FilledButton(
                text="Conectar con X (Twitter)",
                icon=ft.Icons.ADD,
                on_click=self.handle_connect_twitter
            )
        ]
    
    def handle_connect_twitter(self, e):
        print("[SettingsView] El usuario quiere conectar con Twitter. Llamando al manejador principal...")
        self.on_connect_twitter()