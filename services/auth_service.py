from config import supabase

def register_user(email: str, password: str, confirm_password: str):
    if password != confirm_password:
        return {"success": False, "error": "Las contraseñas no coinciden"}
    if len(password) < 6:
        return {"success": False, "error": "La contraseña debe tener al menos 6 caracteres"}
    
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        
        return {"success": True, "data": res}
    
    except Exception as e:
        error_message = str(e)
        if "User already registered" in error_message:
            return {"success": False, "error": "Este correo electrónico ya está registrado."}
        
        return {"success": False, "error": f"Error inesperado {error_message}"}

def login_user(email: str, password: str):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return {"success":True, "data": res}
    except Exception as e:
        error_message = str(e)
        if "Invalid login credentials" in error_message:
            return {"success": False, "error": "Correo o contraseña incorrectos."}
        return {"success": False, "error": f"Error inesperado: {error_message}"}

def logout_user():
    try:
        supabase.auth.sign_out()
        return {"success", True}
    except Exception as e:
        print(f"Error al cerrar sesión: {e}")
        return {"success": False, "error": str(e)}