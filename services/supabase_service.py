from config import supabase
from datetime import datetime
def add_post(content: str, scheduled_at: datetime = None):
    try:
        placeholder_user_id = None
        platform = "X"
        schedule_time = scheduled_at if scheduled_at else datetime.now()
        
        post_data = {
            "user_id": placeholder_user_id,
            "platform": platform,
            "content": content,
            "scheduled_at": schedule_time.isoformat(),
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

def delete_post (post_id: str):
    try:
        data, count = supabase.table("posts").delete().eq("id", post_id).execute()
        if count:
            print(f"Post con ID {post_id} eliminado con éxito.")
            return {"success": True, "data": data}
        else:
            print(f"No se encontró ningún post con ID {post_id} para eliminar.")
            return {"success": False, "error": "Post not found"}
    except Exception as e:
        print(f"Error al eliminar el post {post_id}: {e}")
        return {"success": False, "error": str(e)}

def update_post(post_id: str, new_content: str, new_cheduled_at: datetime):
    try:
        update_data = {
            "content": new_content,
            "scheduled_at": new_cheduled_at.isoformat()
        }
        data, count = supabase.table("posts").update(update_data).eq("id", post_id).execute()
        
        if count:
            print(f"Post con ID {post_id} actualizado con éxito")
            return{"success": True, "data": data}
        else:
            print(f"No se encontró ningún post con ID {post_id} para actualizar.")
            return{"success": False, "error": "Post not found"}
    
    except Exception as e:
        print(f"Error al actualizar el post {post_id}: {e}")
        return {"success": False, "error": str(e)}