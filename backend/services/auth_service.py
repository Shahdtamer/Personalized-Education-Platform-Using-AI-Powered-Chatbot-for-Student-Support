from backend.db.supabase_client import supabase
from fastapi import HTTPException
# Registration
def register(email: str, password: str, full_name: str):

    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        print(response)

        user = response.user

        if not user:
            raise HTTPException(
                status_code=400,
                detail="User creation failed"
            )

        user_id = user.id

        profile_response = supabase.table("profiles").insert({
            "id": user_id,
            "full_name": full_name
        }).execute()

        print(profile_response)

        return {
            "message": "Registered successfully",
            "user_id": user_id
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

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