from config import supabase
from datetime import datetime

def fetch_due_work():
    try:
        now_iso = datetime.now().isoformat()
        work_items = []
        
        posts_res = supabase.table("posts").select("*").eq("status", "scheduled").lte("scheduled_at", now_iso).is_("thread_id", "null").execute()
        
        for post in posts_res.data:
            work_items.append({
                "work_type": "post",
                "data": post
            })
        
        threads_res = supabase.table("threads").select("*").eq("status", "scheduled").lte("scheduled_at",now_iso).execute()
        
        for thread in threads_res.data:
            posts_in_thread_res = supabase.table("posts").select("*").eq("thread_id", thread['id']).order("thread_order", desc=False).execute()
            
            work_items.append({
                "work_type": "thread",
                "data": thread,
                "posts": posts_in_thread_res.data
            })
        
        if work_items:
            print(f"[Scheduler] Se encontraron {len(work_items)} trabajos para procesar.")
        return {"success": True, "data": work_items}
    except Exception as e:
        print(f"[Scheduler] Error al buscar trabajo pendiente: {e}")
        return {"success": False, "error": str(e)}

def update_item_status(item_type: str, item_id: str, new_status: str, error_message: str=None):
    try:
        table_name = "posts" if item_type == "post" else "threads"
        update_data = {"status": new_status}
        
        if error_message:
            # En el futuro, podríamos tener una columna 'error_details'
            # Por ahora, el print es suficiente para depurar
            print(f"[Scheduler] Registrando error para {item_type} {item_id}: {error_message}")
            update_data['last_error'] = error_message
        
        result = supabase.table(table_name).update(update_data).eq("id", item_id).execute()
        
        if item_type == 'thread' and new_status == 'published':
            supabase.table("posts").update({'status': 'published'}).eq('thread_id', item_id).execute()
        return {"success": True, "data": result.data}
    except Exception as e:
        print(f"[Scheduler] Error al actualizar estado del {item_type} {item_id}: {e}")
        return {"success": False, "error": str(e)}
    #TODO: Nota: La nueva función update_item_status asume que podrías tener una columna last_error en tus tablas posts y threads. Esto es una buena práctica. Puedes añadirla con: ALTER TABLE posts ADD COLUMN last_error TEXT; y ALTER TABLE threads ADD COLUMN last_error TEXT;. Por ahora, el código funcionará igual sin ella.