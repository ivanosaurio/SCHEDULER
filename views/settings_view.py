import flet as ft
from theme import TEXT_PRIMARY, TEXT_SECONDARY, BORDER
from components.queue_item import get_platform_details

class SettingsView(ft.Column):
    def __init__(self, on_connect_twitter, connected_accounts :list=None):
        super().__init__()
        self.on_connect_twitter = on_connect_twitter
        self.connected_accounts = connected_accounts if connected_accounts else []
        
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
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        "Cuentas Conectadas",
                        size=18, 
                        width=ft.FontWeight.W_600,
                        color=TEXT_PRIMARY
                        ),
                    ft.FilledButton(
                        text="Conectar con X (Twitter)",
                        icon=ft.Icons.ADD,
                        on_click=self.handle_connect_twitter
                        )
                    ]
                ),
            self.build_accounts_list()
        ]
    
    def build_accounts_list(self):
        if not self.connected_accounts:
            return ft.Container(
                padding=20, 
                border=ft.border.all(1, BORDER),
                border_radius=8,
                content=ft.Text("Aún no has conectado ninguna cuenta.", color=TEXT_SECONDARY)
            )
        
        accoun_cards = [self.create_account_card(acc) for acc in self.connected_accounts]
        return ft.Column(controls=accoun_cards)
    
    def create_account_card(self, account_data: dict):
        platform_details = get_platform_details(account_data.get("platform"))
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
            border=ft.border.all(1, BORDER),
            border_radius=8,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        spacing=15, 
                        controls=[
                            ft.Icon(name=platform_details.get("icon"), color=platform_details.get("color")),
                            ft.Text(f"@{account_data.get('username')}", weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)
                        ]
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Desconectar cuenta (Próximamente)",
                        icon_color=TEXT_SECONDARY,
                        disabled=True
                    )
                ]
            )
        )
    
    def handle_connect_twitter(self, e):
        print("[SettingsView] El usuario quiere conectar con Twitter. Llamando al manejador principal...")
        self.on_connect_twitter()