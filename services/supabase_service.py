from config import supabase
from datetime import datetime
from urllib.parse import urlparse
def add_post(user_id: str, content: str, scheduled_at: datetime = None, image_url: str = None):
    try:
        platform = "X"
        schedule_time = scheduled_at if scheduled_at else datetime.now()
        
        post_data = {
            "user_id": user_id,
            "platform": platform,
            "content": content,
            "scheduled_at": schedule_time.isoformat(),
            "status": "scheduled",
            "image_url": image_url
        }
        data, count = supabase.table("posts").insert(post_data).execute()
        print(f"Exito, se metieron los datos: {data}")
        return {"success":True, "data":data}
    except Exception as e:
        print(f"Error al guardar el post: {e}")
        return {"success": False, "error": str(e)}

def fetch_posts(user_id: str):
    try:
        query_result = supabase.table("posts").select("*").eq('user_id', user_id).order('scheduled_at', desc=False).execute()
        
        post_count = len(query_result.data)
        print(f"Datos de Supabase obtenidos para el usuario{user_id}. Se encontraron {post_count} posts")
        return {"success": True, "data": query_result.data}
    
    except Exception as e:
        print(f"Error al obtener los posts: {e}")
        return {"success": False, "error": str(e)}

def delete_post (post_id: str):
    try:
        post_to_delete_req = supabase.table("posts").select("image_url").eq("id", post_id).single().execute()
        post_data = post_to_delete_req.data
        
        if post_data and post_data.get("image_url"):
            image_url = post_data["image_url"]
            
            parsed_url = urlparse(image_url)
            url_path_clean = parsed_url.path
            
            try:
                object_path = url_path_clean.split("post-images/")[1]
                print(f"Intentando borrar imagen del storage: {object_path}")
                
                supabase.storage.from_("post-images").remove([object_path])
                print("Llamada de borrado a Supabase ejecutada")
            except IndexError:
                print(f"La URL de la imagen no tiene el formato esperado: {image_url}")
        
        data, count = supabase.table("posts").delete().eq("id", post_id).execute()
        if count:
            print(f"Post con ID {post_id} eliminado con éxito de la DB.")
            return {"success": True, "data": data}
        else:
            print(f"No se encontró ningún post con ID {post_id} para eliminar.")
            return {"success": False, "error": "Post not found in DV"}
    except Exception as e:
        print(f"Error al eliminar el post {post_id}: {e}")
        return {"success": False, "error": str(e)}

def update_post(post_id: str, new_content: str, new_scheduled_at: datetime):
    try:
        update_data = {
            "content": new_content,
            "scheduled_at": new_scheduled_at.isoformat()
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

def upload_image(file_path: str, file_name: str):
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
        
        bucket_path =  f"public/{file_name}"
        
        supabase.storage.from_("post-images").upload(
            path=bucket_path,
            file=file_content,
            file_options={"cache-control": "3600", "upsert": "true"}
        )
        
        public_url = supabase.storage.from_("post-images").get_public_url(bucket_path)
        print(f"Imagen subida con éxito. URL: {public_url}")
        return {"success": True, "url": public_url}
    except Exception as e:
        error_message = f"Erro al subir la imagen: {e}"
        print(error_message)
        return {"success": False, "error": error_message}

def save_social_account(user_id: str, platform: str, username: str, access_token: str, access_token_secret: str):
    try:
        account_data = {
            "user_id": user_id,
            "platform": platform,
            "username": username,
            "access_token": access_token, #Encryptar
            "access_token_secret": access_token_secret #Encryptar
        }
        data, count = supabase.table("social_accounts").insert(account_data).execute()
        
        if count:
            print(f"Cuenta de {platform} @{username} guardada exitosamente para el usuario {user_id}")
            return {"success": True, "data": data}
        else:
            return {"success": False, "error": "No se pudo guardar la cuenta."}
    except Exception as e:
        if "duplicate key value violates unique constraint" in str(e):
            error_msg = f"La cuenta @{username} ya está conectada."
            print(f"[SupabaseService] Error: {error_msg}")
            return {"success": False, "error": error_msg}
        
        print (f"[SupabaseService] Error al guardar la cuenta: {e}")
        return {"success": False, "error": str(e)}

def fetch_social_accounts(user_id: str):
    try:
        accounts = supabase.table("social_accounts").select("id, platform, username").eq("user_id", user_id).execute()
        return {"success": True, "data": accounts.data}
    except Exception as e:
        print(f"[SupabaseService] Error al obtener las cuentas sociales: {e}")
        return {"success": False, "error": str(e)}