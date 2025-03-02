from fastapi import APIRouter
from app.schemas.users import UserLoginRequest
router = APIRouter()

@router.post("/auth/login")
async def login(UserLoginRequest : UserLoginRequest):
    return {
        "message": "Hello, from login!",
        "data": UserLoginRequest
    }