from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def read_root():
    return {"message": "Hello, from products!"}