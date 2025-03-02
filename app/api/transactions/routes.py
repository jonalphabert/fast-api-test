from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import get_db
from app.services.transaction import get_transaction, get_transaction_by_id, get_transaction_detail_by_id_transaction
from app.schemas.transaction import TransactionSchema, TransactionAndDetailSchema

router = APIRouter()

@router.get("/transactions")
async def read_root(db: Session = Depends(get_db)) -> dict[str, list[TransactionSchema]]:
    transaction_list = get_transaction(db)
    return {"data": transaction_list}

@router.get("/transactions/{transaction_id}")
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)) -> TransactionAndDetailSchema:
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="transaction not found")

    transaction_detail_list = get_transaction_detail_by_id_transaction(db, transaction_id)
    return {
        "transaction_info": transaction,
        "transaction_details": transaction_detail_list
    }