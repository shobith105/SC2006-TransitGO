from app.config import settings
from supabase import create_client, Client

supabase: Client=create_client(settings.SUPABASE_URL,settings.SUPABASE_KEY)

def get_specific_user(user_id: int):
    resp = supabase.table("users").select("username").eq("id",user_id).single().execute()
    return resp