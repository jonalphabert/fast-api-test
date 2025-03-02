from fastapi import APIRouter
from app.schemas.users import UserLoginRequest
router = APIRouter()

@router.get("/auth")
async def read_root():
    return {"message": "Hello, from auth!"}

@router.post("/auth/login")
async def login(UserLoginRequest : UserLoginRequest):
    return {
        "message": "Hello, from login!",
        "data": UserLoginRequest
    }