from backend.db.supabase_client import supabase
from fastapi import HTTPException
# Registration
def register(email: str, password: str, full_name: str):

    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        user = response.user

        if not user:
            raise HTTPException(
                status_code=400,
                detail="User creation failed in Supabase Auth"
            )

        user_id = user.id

        supabase.table("profiles").insert({
            "id": user_id,
            "full_name": full_name
        }).execute()

        return {"message": "Registered successfully", "user_id": user_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Registered successfully", "user_id": user_id}

# Login
def login(email: str, password: str):

    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    session = response.session
    user = response.user

    return {
        "access_token": session.access_token,
        "user_id": user.id
    }

# Logout
def logout():
    supabase.auth.sign_out()
    return {"message": "Logged out successfully"}