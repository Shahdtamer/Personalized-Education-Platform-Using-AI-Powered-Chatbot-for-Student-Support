from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.auth_service import register, login, logout

router = APIRouter()
class RegisterRequest(BaseModel):
    email:str
    password:str
    full_name:str
class LoginRequest(BaseModel):
    email: str
    password: str
@router.post("/register")
def register_route(req: RegisterRequest):
    return register(req.email, req.password, req.full_name)

@router.post("/login")
def login_route(req: LoginRequest):
    return login(req.email, req.password)

@router.post("/logout")
def logout_route():
    return logout()