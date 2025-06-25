import os, tweepy, requests, tempfile
from config import supabase

API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET = os.environ.get("TWITTER_API_SECRET")
CALLBACK_URL = "http://127.0.0.1:8080/callback"

def get_twitter_auth_url():
    if not API_KEY or not API_SECRET:
        return {"success": False, "error": "Credenciales de la API de Twitter no configuradas"}
    
    try:
        oauth1_user_handler = tweepy.OAuth1UserHandler(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            callback=CALLBACK_URL
        )
        auth_url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)
        return {"success": True, "auth_url": auth_url, "handler": oauth1_user_handler}
    except Exception as e:
        print(f"[TwitterService] Error al obtener la URL de autorización: {e}")
        return {"success": False, "error": str(e)}

def get_twitter_access_token(handler: tweepy.OAuth1UserHandler, oauth_verifier: str):
    try:
        access_token, access_token_secret = handler.get_access_token(oauth_verifier)
        auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, access_token, access_token_secret)
        api = tweepy.API(auth)
        
        user_info = api.verify_credentials()
        username = user_info.screen_name
        
        profile_image_url = user_info.profile_image_url_https.replace("_normal", "")
        return {
            "success": True,
            "username": username,
            "access_token": access_token,
            "access_token_secret": access_token_secret,
            "profile_image_url": profile_image_url
        }
    except Exception as e:
        print(f"[TwitterService] Error al obtener el token de acceso: {e}")
        return {"success": False, "error": str(e)}

def publish_post_to_twitter(post_data: dict, account_data: dict):
    try:
        content = post_data.get("content")
        image_url = post_data.get("image_url")
        access_token = account_data.get("access_token")
        access_token_secret = account_data.get("access_token_secret")
        
        if not all([API_KEY, API_SECRET, access_token, access_token_secret]):
            return {"success": False, "error": "Faltan credenciales de atenticación para publicar"}
        
        auth_v1 = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, access_token, access_token_secret)
        api_v1 = tweepy.API(auth_v1)
        
        client_v2 = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        media_id = None
        
        if image_url:
            print(f"[TwitterService] Descargando imagen desde: {image_url}")
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            
            with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as temp_file:
                for chunk in response.iter_content(chunk_size=8192):
                    temp_file.write(chunk)
                temp_file.seek(0)
                
                print(f"[TwitterService] Imagen descargada en archivo temporal. Subiendo a Twitter...")
                
                media = api_v1.media_upload(filename=temp_file.name)
                media_id = media.media_id
                print(f"[TwitterService] Imagen subida. Media ID: {media_id}")
        
        tweet_params = {"text": content}
        if media_id:
            tweet_params["media_ids"] = [media_id]
        
        print(f"[TwitterService] Publicando tweet con parámetros: {tweet_params}")
        response = client_v2.create_tweet(**tweet_params)
        print(f"[TwitterService] Tweet publicado con éxito. Respuesta: {response.data}")
        
        return {"success": True, "data": response.data}
    
    except Exception as e:
        error_message = f"Error al publicar en Twitter: {e}"
        print(error_message)
        return {"success": False, "error": error_message}