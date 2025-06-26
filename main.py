import flet as ft
import json, threading, time, queue, http.server, socketserver, webbrowser, asyncio
from urllib.parse import urlparse, parse_qs
from theme import BACKGROUND, APP_THEME
from views.dashboard_view import DashboardView
from auth.login_view import LoginView
from auth.register_view import RegisterView
from services.auth_service import register_user, login_user, logout_user, set_user_session
from services.scheduler_service import fetch_due_work, update_item_status
from services import twitter_service, supabase_service

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.auth_queue = kwargs.pop("auth_queue")
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/callback":
            query_params = parse_qs(parsed_path.query)
            oauth_verifier = query_params.get('oauth_verifier', None)[0]
            
            if oauth_verifier:
                self.auth_queue.put({"success": True, "oauth_verifier": oauth_verifier})
                
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><head><title>Autenticacion Exitosa</title></head>")
                self.wfile.write(b"<body><p>Genial! La autenticacion con Twitter fue exitosa.</p>")
                self.wfile.write(b"<p>Puedes cerrar esta ventana y volver a la aplicacion.</p></body></html>")
            else:
                error_msg = query_params.get('error_description', ["Ocurrio un error desconocido."])[0]
                
                self.auth_queue.put({"success": False, "error": error_msg})
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"<html><body><h1>Error</h1><p>{error_msg}</p></body></html>".encode())
        else:
            self.send_response(404)
            self.end_headers()

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.app_instance = self
        self.page.title ="Social Scheduler"
        self.page.bgcolor = BACKGROUND
        self.page.theme = APP_THEME
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.START
        
        #Sesión usuario
        self.user_session = None
        self.scheduler_thread = None
        self.stop_scheduler_event = threading.Event()
        
        #Autenticacion
        self.auth_queue = queue.Queue()
        self.temp_oauth_handler = None
        self.http_server_thread = None
        self.start_http_server()
        
        self.login_view = LoginView(
            on_login_submit=self.handle_login_submit,
            on_navigate_to_register=self.go_to_register
        )
        
        self.register_view = RegisterView(
            on_register_submit=self.handle_register_submit,
            on_navigate_to_login=self.go_to_login
        )
        
        self.dashboard_view = None
        self.page.run_task(self.check_auth_queue)
        
        self.load_initial_view()
    
    def start_http_server(self):
        def handler_factory(*args, **kwargs):
            return CallbackHandler(*args, auth_queue=self.auth_queue, **kwargs)
        
        PORT = 8080
        httpd = socketserver.TCPServer(("", PORT), handler_factory)
        
        self.http_server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        self.http_server_thread.start()
        print(f"[App] Micro-servidor HTTP iniciado en el puerto {PORT}")
    
    async def check_auth_queue(self):
        while True:
            try:
                result = self.auth_queue.get_nowait()
                if self.dashboard_view:
                    await self.dashboard_view.process_twitter_callback(result)
            except queue.Empty:
                pass
            await asyncio.sleep(1)
    
    def handle_connect_twitter(self):
        print("[App] El usuario quiere conectar con Twitter. Obteniendo URL de autorización...")
        result = twitter_service.get_twitter_auth_url()
        
        if result.get("success"):
            self.temp_oauth_handler = result["handler"]
            auth_url = result["auth_url"]
            print(f"[App] URL de autorización obtenida. Abriendo en el navegador: {auth_url}")
            self.page.launch_url(auth_url)
        else:
            if self.dashboard_view:
                self.dashboard_view.show_feedback(f"Error: {result.get('error')}", is_error=True)
    
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
            self.dashboard_view = DashboardView(self.page, user_id, on_logout=self.handle_logout, on_connect_twitter=self.handle_connect_twitter)
        self.change_view(self.dashboard_view)
    
    def run_scheduler(self):
        print("[Scheduler] Proceso de planificación iniciado.")
        while not self.stop_scheduler_event.is_set():
            result = fetch_due_work()
            if result.get("success") and result.get("data"):
                due_items = result["data"]
                print(f"[Scheduler] Se encontraron {len(due_items)} trabajos pendientes.")
                
                for item in due_items:
                    item_data = item.get("data", {})
                    item_type = item.get("work_type")
                    item_id = item_data.get("id")
                    user_id = item_data.get("user_id")
                    platform = item_data.get("platform")
                    
                    print(f"[Scheduler] Procesando {item_type} ID: {item_id} para la plataforma: {platform}")
                    
                    account_result = supabase_service.fetch_social_accounts(user_id)
                    
                    if not account_result.get("success"):
                        error_msg = f"No se pudieron obtener las cuentas sociales para el usuario {user_id}."
                        print(f"[Scheduler] {error_msg}")
                        update_item_status(item_type, item_id, "error", error_msg)
                        continue
                    
                    target_account = next((acc for acc in account_result.get("data", []) if acc.get("platform") == platform), None)
                    
                    if not target_account:
                        error_msg = f"No se encontró una cuenta conectada de '{platform}' para el {item_type} {item_id}."
                        print(f"[Scheduler] {error_msg}")
                        update_item_status(item_type, item_id, "error", error_msg)
                        continue
                    
                    publish_result = None
                    if platform =="x":
                        if item_type == "post":
                            publish_result = twitter_service.publish_post_to_twitter(item_data, target_account)
                        elif item_type == "thread":
                            posts_in_thread = item.get("posts", [])
                            publish_result = twitter_service.publish_thread(posts_in_thread, target_account)
                    else:
                        error_msg = f"Plataforma '{platform}' no soportada para publicación."
                        print(f"[Scheduler] {error_msg}")
                        update_item_status(item_type, item_id, "error", error_msg)
                        continue
                    
                    if publish_result and publish_result.get("success"):
                        print(f"[Scheduler] {item_type.capitalize()} {item_id} publicado con éxito en {platform.capitalize()}.")
                        update_item_status(item_type, item_id, "published")
                    else:
                        error_msg = publish_result.get("error", f"Error desconocido al publicar {item_type}.")
                        print(f"[Scheduler] Fallo al publicar {item_type} {item_id}: {error_msg}")
                        update_item_status(item_type, item_id, "error", error_msg)
                    
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
            if self.user_session and self.user_session.session:
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
        
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join(timeout=5)
            print("[Scheduler] Hilo del planificador detenido con éxito.")
        self.go_to_login()
        print("Cierre de sesión completado. Redirigiendo a login.")

def main(page: ft.Page):
    App(page)

if __name__ == "__main__":
    ft.app(target=main)