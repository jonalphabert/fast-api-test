from fastapi import APIRouter

router = APIRouter()

@router.get("/transactions")
async def read_root():
    return {"message": "Hello, from transactions!"}