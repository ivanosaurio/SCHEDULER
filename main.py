import flet as ft
import json, threading, time
from theme import BACKGROUND, APP_THEME
from views.dashboard_view import DashboardView
from auth.login_view import LoginView
from auth.register_view import RegisterView
from services.auth_service import register_user, login_user, logout_user, set_user_session
from services.scheduler_service import fetch_due_posts, update_post_status

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
        self.scheduler_thread = None
        self.stop_scheduler_event = threading.Event()
        
        self.login_view = LoginView(
            on_login_submit=self.handle_login_submit,
            on_navigate_to_register=self.go_to_register
        )
        
        self.register_view = RegisterView(
            on_register_submit=self.handle_register_submit,
            on_navigate_to_login=self.go_to_login
        )
        
        self.dashboard_view = None
        
        self.load_initial_view()
    
    def load_initial_view(self):
        print("Buscando sesión de usuario guardada...")
        saved_session_str = self.page.client_storage.get("user_session")
        if saved_session_str:
            session_data = json.loads(saved_session_str)
            print("Sesión encontrada. Intentando restaurar...")
            result = set_user_session(session_data)
            if result.get("success"):
                print("¡Sesión restaurada con éxito!")
                self.user_session = result["data"]
                if not self.scheduler_thread or not self.scheduler_thread.is_alive():
                    self.stop_scheduler_event.clear()
                    self.scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
                    self.scheduler_thread.start()
                self.go_to_dashboard()
                return
        print("No se encontró una sesión válida. Modtrando pantalla de login.")
        self.go_to_login()
    
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
            user_id = self.user_session.user.id
            self.dashboard_view = DashboardView(self.page, user_id, on_logout=self.handle_logout)
        self.change_view(self.dashboard_view)
    
    def run_scheduler(self):
        while not self.stop_scheduler_event.is_set():
            result = fetch_due_posts()
            if result.get("success"):
                for post in result["data"]:
                    post_id = post.get("id")
                    print(f"[Scheduler] Procesando post ID: {post_id}")
                    # Aquí es donde, en el futuro, llamaríamos a la API de X/Twitter.
                    update_post_status(post_id, "published")
                    if self.dashboard_view:
                        self.page.run_task(self.dashboard_view.load_queue_posts)
            self.stop_scheduler_event.wait(60)
        print("[Scheduler] Proceso de planificación detenido.")
    
    def handle_login_submit(self, email: str, password: str):
        print(f"Intento de inicio de sesión con Email {email}, Contraseña: {'*' * len(password)}")
        self.login_view.show_feedback("Verificando...", is_error=False)
        
        result = login_user(email, password)
        
        if result["success"]:
            self.user_session = result["data"]
            print("¡Inicio de sesión exitoso!")
            session_obj = {
                "access_token": self.user_session.session.access_token,
                "refresh_token": self.user_session.session.refresh_token
            }
            self.page.client_storage.set("user_session", json.dumps(session_obj))
            print("Sesión guardada en el almacenamiento del cliente.")
            
            if not self.scheduler_thread or not self.scheduler_thread.is_alive():
                self.stop_scheduler_event.clear()
                self.scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
                self.scheduler_thread.start()
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
    
    def handle_logout(self, e=None):
        print("[Scheduler] Solicitando detención del planificador...")
        self.stop_scheduler_event.set()
        print("Iniciando proceso de cierre de sesión...")
        
        self.page.client_storage.remove("user_session")
        print("Sesión eliminada del almacenamiento del cliente.")
        
        logout_user()
        self.user_session = None
        self.dashboard_view = None
        self.go_to_login()
        print("Cierre de sesión completado. Redirigiendo a login.")

def main(page: ft.Page):
    App(page)

if __name__ == "__main__":
    ft.app(target=main)