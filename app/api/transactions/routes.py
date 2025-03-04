from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import get_db
from app.services.transaction import get_transaction, get_transaction_by_id, get_transaction_detail_by_id_transaction, create_transaction_data, create_transaction_detail
from app.schemas.transaction import TransactionSchema, TransactionAndDetailSchema, TransactionNewRecordSchema
from app.api.middlewareAuth import get_current_user

router = APIRouter()

@router.get("/transactions", dependencies=[Depends(get_current_user)])
async def read_root(db: Session = Depends(get_db)) -> dict[str, list[TransactionSchema]]:
    transaction_list = get_transaction(db)
    return {"data": transaction_list}

@router.get("/transactions/{transaction_id}", dependencies=[Depends(get_current_user)])
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)) -> TransactionAndDetailSchema:
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="transaction not found")

    transaction_detail_list = get_transaction_detail_by_id_transaction(db, transaction_id)
    return {
        "transaction_info": transaction,
        "transaction_details": transaction_detail_list
    }

@router.post("/transactions", dependencies=[Depends(get_current_user)])
async def create_transaction(transaction: TransactionNewRecordSchema, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        print(current_user["user_id"])
        new_transaction = create_transaction_data(db, current_user["user_id"])
        transaction_detail = create_transaction_detail(db, transaction.transaction_details, new_transaction.transaction_id)
        return {"success": True}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")