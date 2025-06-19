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
        print(f"Exito, se metieron los datos: {data}")
        return {"success":True, "data":data}
    except Exception as e:
        print(f"Error al guardar el post: {e}")
        return {"success": False, "error": str(e)}

def fetch_posts():
    try:
        query_result = supabase.table("posts").select("*").is_('user_id', None).order('scheduled_at', desc=False).execute()
        
        post_count = len(query_result.data)
        print(f"Datos de Supabase obtenidos con éxito. Se encontraron {post_count} posts.")
        return {"success": True, "data": query_result.data}
    
    except Exception as e:
        print(f"Error al obtener los posts: {e}")
        return {"success": False, "error": str(e)}