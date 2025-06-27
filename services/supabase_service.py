from config import supabase
from datetime import datetime
from urllib.parse import urlparse

def add_thread(user_id: str, platform: str, scheduled_at: datetime, posts_content: list[str]):
    try:
        thread_entry = {
            "user_id": user_id,
            "platform": platform,
            "scheduled_at": scheduled_at.isoformat(),
            "status": "scheduled"
        }
        thread_res = supabase.table("threads").insert(thread_entry).execute()
        
        if not thread_res.data:
            raise Exception("No se pudo crear la entrada principal del hilo.")
        
        thread_id = thread_res.data[0]["id"]
        print(f"Hilo creado con ID: {thread_id}")
        
        posts_to_insert = []
        
        for index, content in enumerate(posts_content):
            if content.strip():
                posts_to_insert.append({
                    "user_id": user_id,
                    "platform": platform,
                    "content": content,
                    "thread_id": thread_id,
                    "thread_order": index,
                    "status": "scheduled",
                    "image_url": None
                })
        
        if posts_to_insert:
            posts_res = supabase.table("posts").insert(posts_to_insert).execute()
            print(f"Insertados {len(posts_res.data)} posts para el hilo {thread_id}")
        
        return {"success": True, "data": thread_res.data}
    except Exception as e:
        print(f"Error al guardar el hilo: {e}")
        return {"success": False, "error": str(e)}

def add_post(user_id: str, content: str, scheduled_at: datetime = None, image_url: str = None):
    try:
        platform = "x"
        schedule_time = scheduled_at if scheduled_at else datetime.now()
        
        post_data = {
            "user_id": user_id,
            "platform": platform,
            "content": content,
            "scheduled_at": schedule_time.isoformat(),
            "status": "scheduled",
            "image_url": image_url,
            "thread_id": None,
            "thread_order": None
        }
        data, count = supabase.table("posts").insert(post_data).execute()
        print(f"Exito, se metieron los datos: {data}")
        return {"success":True, "data":data}
    except Exception as e:
        print(f"Error al guardar el post: {e}")
        return {"success": False, "error": str(e)}

def fetch_posts(user_id: str):
    try:
        accounts_res = supabase.table("social_accounts").select("*").eq('user_id', user_id).execute()
        
        if not accounts_res.data:
            return {"success": True, "data": []}
        
        account_map = {acc['platform'].lower(): acc for acc in accounts_res.data}
        
        post_res = supabase.table("posts").select("*").eq('user_id', user_id).order('scheduled_at', desc=False, nullsfirst=False).order('created_at', desc=False).execute()
        
        for post in post_res.data:
            platform = post.get("platform").lower()
            if platform in account_map:
                post['account_details'] = account_map[platform]
        
        post_count = len(post_res.data)
        print(f"Datos de Supabase obtenidos para el usuario {user_id}. Se encontraron {post_count} posts.")
        
        return {"success": True, "data": post_res.data}
    except Exception as e:
        print(f"Error al obtener los posts: {e}")
        return {"success": False, "error": str(e)}

def delete_post (post_id: str):
    try:
        post_to_delete_req = supabase.table("posts").select("image_url").eq("id", post_id).single().execute()
        post_data = post_to_delete_req.data
        
        if post_data and post_data.get("thread_id"):
            thread_id = post_data["thread_id"]
            print(f"El post {post_id} pertenece al hilo {thread_id}. Se eliminará el hilo completo.")
            
            supabase.table("threads").delete().eq("id", thread_id).execute()
            print(f"Hilo {thread_id} eliminado.")
            # Aquí podríamos querer borrar imágenes de todos los posts del hilo si las tuvieran.
        else:
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
            if not count:
                print(f"No se encontró ningún post con ID {post_id} para eliminar.")
                return {"success": False, "error": "Post not found in DB"}
        return {"success": True}
    except Exception as e:
        print(f"Error al eliminar el post {post_id}: {e}")
        return {"success": False, "error": str(e)}

def update_post(post_id: str, new_content: str, new_scheduled_at: datetime):
    try:
        update_data = {
            "content": new_content,
            "scheduled_at": new_scheduled_at.isoformat()
        }
        if new_scheduled_at:
            update_data["scheduled_at"] = new_scheduled_at.isoformat()
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

def save_social_account(user_id: str, platform: str, username: str, access_token: str, access_token_secret: str, profile_image_url: str):
    try:
        account_data = {
            "user_id": user_id,
            "platform": platform.lower(),
            "username": username,
            "access_token": access_token, #Encryptar
            "access_token_secret": access_token_secret, #Encryptar
            "profile_image_url": profile_image_url
        }
        data, count = supabase.table("social_accounts").upsert(account_data, on_conflict="user_id, platform").execute()
        
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
        accounts = supabase.table("social_accounts").select("*").eq("user_id", user_id).execute()
        print(f"[SupabaseService] Obtenidas {len(accounts.data)} cuentas sociales para el usuario {user_id}.")
        return {"success": True, "data": accounts.data}
    except Exception as e:
        print(f"[SupabaseService] Error al obtener las cuentas sociales: {e}")
        return {"success": False, "error": str(e)}