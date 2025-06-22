import flet as ft
from theme import BACKGROUND, SURFACE, PRIMARY, TEXT_PRIMARY, TEXT_SECONDARY, BORDER

class RegisterView(ft.Column):
    def __init__(self, on_register_submit, on_navigate_to_login):
        super().__init__()
        
        #Callback
        self.on_register_submit = on_register_submit
        self.on_navigate_to_login = on_navigate_to_login
        
        #Configuración General
        self.alignment =ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand= True
        self.spacing = 30
        
        #Controles
        self.feedback_text = ft.Text(
            value="",
            color=ft.Colors.RED_500,
            visible=False
        )
        
        self.email_field = ft.TextField(
            label="Correo Electrónico",
            hint_text="tu.nuevo.email@ejemplo.com",
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
        
        self.confirm_password_field = ft.TextField(
            label="Confirmar Contraseña",
            password=True,
            can_reveal_password=True,
            width=320,
            border_color=BORDER,
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            label_style=ft.TextStyle(color=TEXT_SECONDARY)
        )
        
        self.register_button = ft.FilledButton(
            text="Crear Cuenta",
            width=320, 
            height=45,
            on_click=self.handle_register_click
        )
        
        self.login_link = ft.Row(
            width=320, 
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("¿Ya tienes una cuenta?", color=TEXT_SECONDARY, size=14),
                ft.TextButton("Inicia Sesión", on_click=self.on_navigate_to_login)
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
                    ft.Text("Crea tu Cuenta", size=24, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                    self.email_field,
                    self.password_field,
                    self.confirm_password_field,
                    self.feedback_text,
                    self.register_button,
                    ft.Divider(height=10, color="transparent"),
                    self.login_link
                ]
            )
        )
        
        self.controls = [form_container]
    
    def handle_register_click(self, e):
        email = self.email_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value
        self.on_register_submit(email, password, confirm_password)
    
    def show_feedback(self, message: str, is_error: bool=True):
        self.feedback_text.value = message
        self.feedback_text.color = ft.Colors.RED_500 if is_error else ft.Colors.GREEN_500
        self.feedback_text.visible = True
        self.update()