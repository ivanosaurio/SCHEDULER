import flet as ft
from theme import BACKGROUND, SURFACE, PRIMARY, TEXT_PRIMARY, TEXT_SECONDARY, BORDER

class LoginView(ft.Column):
    def __init__(self, on_login_submit, on_navigate_to_register):
        super().__init__()
        
        #Callback
        self.on_login_submit = on_login_submit
        self.on_navigate_to_register = on_navigate_to_register
        
        #Configuración general
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.spacing = 30
        
        #Controles
        self.email_field = ft.TextField(
            label="Corre Electrónico",
            width=320,
            border_color=BORDER,
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            label_style=ft.TextStyle(color=TEXT_SECONDARY)
        )
        
        self.password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            width=320,
            border_color=BORDER,
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            label_style=ft.TextStyle(color=TEXT_SECONDARY)
        )
        
        self.login_button = ft.FilledButton(
            text="Iniciar Sesión",
            width=320,
            height=45,
            on_click=self.handle_login_click
        )
        
        self.register_link = ft.Row(
            width=320,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("¿No tienes una cuenta?", color=TEXT_SECONDARY),
                ft.TextButton(
                    "Regístrate",
                    on_click=self.on_navigate_to_register
                )
            ]
        )
        
        form_container = ft.Container(
            padding=40,
            border_radius=12,
            bgcolor=SURFACE,
            content=ft.Column(
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Bienvenido de Nuevo",
                        size=24,
                        weight=ft.FontWeight.W_600,
                        color=TEXT_PRIMARY
                    ),
                    self.email_field,
                    self.password_field,
                    self.login_button,
                    ft.Divider(height=10, color="transparent"),
                    self.register_link
                ]
            )
        )
        
        self.controls = [form_container]
    
    def handle_login_click(self, e):
        email = self.email_field.value
        password = self.password_field.value
        self.on_login_submit(email, password)