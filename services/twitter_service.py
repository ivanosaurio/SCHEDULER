import os, tweepy
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