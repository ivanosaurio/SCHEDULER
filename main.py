import flet as ft
from theme import BACKGROUND, APP_THEME
from views.dashboard_view import DashboardView
from auth.login_view import LoginView
from auth.register_view import RegisterView
from services.auth_service import register_user,login_user

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title ="Social Scheduler"
        self.page.bgcolor = BACKGROUND
        self.page.theme = APP_THEME
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.START
        
        #Sesión usuario
        self.user_session = None
        
        self.login_view = LoginView(
            on_login_submit=self.handle_login_submit,
            on_navigate_to_register=self.go_to_register
        )
        
        self.register_view = RegisterView(
            on_register_submit=self.handle_register_submit,
            on_navigate_to_login=self.go_to_login
        )
        
        self.dashboard_view = None
    
    def change_view(self, new_view: ft.Control):
        self.page.clean()
        self.page.add(new_view)
        self.page.update()
    
    def go_to_login(self, e=None):
        self.change_view(self.login_view)
    
    def go_to_register(self, e=None):
        self.change_view(self.register_view)
    
    def go_to_dashboard(self):
        if not self.dashboard_view:
            self.dashboard_view = DashboardView(self.page)
        self.change_view(self.dashboard_view)
    
    def handle_login_submit(self, email: str, password: str):
        print(f"Intento de inicio de sesión con Email {email}, Contraseña: {'*' * len(password)}")
        self.login_view.show_feedback("Verificando...", is_error=False)
        
        result = login_user(email, password)
        
        if result["success"]:
            self.user_session = result["data"]
            print("¡Inicio de sesión exitoso!")
            self.go_to_dashboard()
        else:
            print(f"Error de inicio de sesión: {result['error']}")
            self.login_view.show_feedback(result["error"])
    
    def handle_register_submit(self, email: str, password: str, confirm_password: str):
        print(f"Llamando a Supabase para registrar a {email}")
        self.register_view.show_feedback("Registrando...", is_error=False)
        
        result = register_user(email, password, confirm_password)
        
        if result["success"]:
            print("¡Registro exitoso!")
            self.register_view.show_feedback("¡Registro exitoso! Revisa tu email para confirmar la cuenta.", is_error=False)
        else:
            print(f"Error de registro: {result['error']}")
            self.register_view.show_feedback(result["error"])

def main(page: ft.Page):
    app_controller = App(page)
    app_controller.go_to_login()

if __name__ == "__main__":
    ft.app(target=main)