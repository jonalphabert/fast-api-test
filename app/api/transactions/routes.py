from fastapi import APIRouter

router = APIRouter()

@router.get("/transactions")
async def read_root():
    return {"message": "Hello, from transactions!"}

@router.get("/transactions/{transaction_id}")
async def read_transaction(transaction_id: int):
    return {"transaction_id": transaction_id}

@router.post("/transactions")
async def create_transaction():
    return {"message": "Hello, from create transaction!"}