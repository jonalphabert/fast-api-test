from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
async def read_root():
    return {"message": "Hello, from auth!"}