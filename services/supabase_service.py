from config import supabase
from datetime import datetime
def add_post(content: str):
    try:
        placeholder_user_id = None
        platform = "X"
        scheduled_at = datetime.now().isoformat()
        
        post_data = {
            "user_id": placeholder_user_id,
            "platform": platform,
            "content": content,
            "scheduled_at": scheduled_at,
            "status": "scheduled"
        }
        data, count = supabase.table("posts").insert(post_data).execute()
        print(f"Exito, se metio los datos: {data}")
        return {"success":True, "data":data}
    except Exception as e:
        print(f"Error al guardar el post: {e}")
        return {"success": False, "error": str(e)}