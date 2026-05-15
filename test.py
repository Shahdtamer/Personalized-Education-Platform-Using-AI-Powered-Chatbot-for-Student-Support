from backend.db.supabase_client import supabase
#to manage to write email disable RLS temporary(for testing only)
auth_response = supabase.auth.sign_up({    #to manage to write emain disable confirmation email
    "email": "yassin568@gmail.com",
    "password": "4654164hgySf"
})

user_id = auth_response.user.id

response = supabase.table("profiles").insert({
    "id": user_id,
    "full_name": "Ahmed Tamer",
    "academic_level": "4th year"
}).execute()

print(response.data)