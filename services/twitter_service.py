import os, tweepy
from config import supabase

API_KEY = os.environ.get("TWITTER_API_ID")
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
        # MUY IMPORTANTE: Necesitaremos el 'request token' en el siguiente paso.
        # Por ahora, lo imprimiremos. En una implementación real, lo guardaríamos temporalmente.
        print(f"[TwitterService] Request Token: {oauth1_user_handler.request_token['oauth_token']}")
        print((f"[TwitterService] Request Token Secret: {oauth1_user_handler.request_token['oauth_token_secret']}"))
        
        return {"success": True, "auth_url": auth_url, "handler": oauth1_user_handler}
    except Exception as e:
        print(f"[TwitterService] Error al obtener la URL de autorización: {e}")
        return {"success": False, "error": str(e)}

# TODO: Crear una función para manejar el callback y obtener el access_token final.
# def get_twitter_access_token(handler, oauth_verifier):
#     ...