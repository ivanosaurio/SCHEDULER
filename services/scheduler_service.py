from config import supabase
from datetime import datetime

def fetch_due_posts():
    try:
        now_iso = datetime.now().isoformat()
        
        result = supabase.table("posts").select("*").eq("status", "scheduled").lte("scheduled_at", now_iso).execute()
        
        print(f"[Scheduler] Se encontraron {len(result.data)} posts para publicar.")
        
        return {"success": True, "data": result.data}
    except Exception as e:
        print(f"[Scheduler] Error al buscar posts: {e}")
        return {"success": False, "error": str(e)}

def update_post_status(post_id: str, new_status: str, error_message: str=None):
    try:
        update_data = {"status": new_status}
        if error_message:
            #En el futuro, podríamos tener una columna 'error_details'
            print(f"[Scheduler] Registrando error para post {post_id}: {error_message}")
            
        result = supabase.table("posts").update(update_data).eq("id", post_id).execute()
        return {"success": True, "data": result.data}
    
    except Exception as e:
        print(f"[Scheduler] Error al actualizar estado del post {post_id}: {e}")
        return {"success": False, "error": str(e)}