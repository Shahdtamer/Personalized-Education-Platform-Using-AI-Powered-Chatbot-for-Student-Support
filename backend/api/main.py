from fastapi import FastAPI
from .auth_routes import router as auth_router
from .chat_routes import router as chat_router

app = FastAPI(title="EduAgent API")

app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "EduAgent API is running"}