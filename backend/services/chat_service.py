from backend.db.supabase_client import supabase

def save_message(session_id: str, role: str, content: str):
    supabase.table("chat_history").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()

def get_history(session_id: str):
    response = supabase.table("chat_history")\
        .select("*")\
        .eq("session_id", session_id)\
        .order("created_at")\
        .execute()
    return response.data

def create_session(user_id: str, title: str = "New Chat"):
    response = supabase.table("sessions").insert({
        "user_id": user_id,
        "title": title
    }).execute()
    return response.data[0]["id"] #to get the id of the newest session