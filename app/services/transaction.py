from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.transaction import TransactionSchema, TransactionDetailSchema
from app.models import Transaction, TransactionDetail
from app.services.product import check_and_update_stock

def get_transaction(db: Session):
    sql = text("""
        SELECT 
            transactions.transaction_id, 
            transactions.transaction_date, 
            transactions.transaction_operator, 
            users.name
        FROM transactions
        INNER JOIN users ON transactions.transaction_operator = users.user_id
    """)

    result = db.execute(sql)
    transactions = result.fetchall()

    transaction_dict = [
        TransactionSchema(
            transaction_id= row.transaction_id,
            transaction_date= row.transaction_date,
            transaction_operator= row.transaction_operator,
            user_name= row.name,
        )
        for row in transactions
    ]

    return transaction_dict

def get_transaction_by_id(db: Session, transaction_id: int):
    sql = text("""
        SELECT 
            transactions.transaction_id, 
            transactions.transaction_date, 
            transactions.transaction_operator, 
            users.name
        FROM transactions
        INNER JOIN users ON transactions.transaction_operator = users.user_id
        WHERE transactions.transaction_id = :transaction_id
    """)

    result = db.execute(sql, {"transaction_id": transaction_id})
    transaction = result.fetchone()

    if transaction:
        transaction_result = TransactionSchema(
            transaction_id= transaction.transaction_id,
            transaction_date= transaction.transaction_date,
            transaction_operator= transaction.transaction_operator,
            user_name= transaction.name,
        )
        return transaction_result

    return None

def get_transaction_detail_by_id_transaction(db: Session, transaction_id: int):
    sql = text("""
        SELECT
            transaction_details.transaction_detail_id,
            transaction_details.transaction_detail_transaction,
            transaction_details.transaction_detail_product,
            transaction_details.transaction_detail_quantity,
            transaction_details.transaction_detail_price,
            transaction_details.transaction_detail_subtotal,
            products.product_name as transaction_product_name
        FROM transaction_details
        INNER JOIN products ON transaction_details.transaction_detail_product = products.product_id
        WHERE transaction_detail_transaction = :transaction_id
    """)

    result = db.execute(sql, {"transaction_id": transaction_id}) 

    transaction_details = result.fetchall()

    if transaction_details:
        transaction_details_dict = [
            TransactionDetailSchema(
                transaction_detail_id=row.transaction_detail_id,
                transaction_detail_transaction=row.transaction_detail_transaction,
                transaction_detail_product=row.transaction_detail_product,
                transaction_detail_quantity=row.transaction_detail_quantity,
                transaction_detail_price=row.transaction_detail_price,
                transaction_detail_subtotal=row.transaction_detail_subtotal,
                transaction_product_name=row.transaction_product_name
            )
            for row in transaction_details
        ]
        return transaction_details_dict
        
    return None


def create_transaction_data(db: Session, user: int):
    try:
        db_transaction = Transaction(
            transaction_operator=user
        )
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create transaction")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

def create_transaction_detail(db: Session, transaction_details: list, id_transaction: int):
    db_transaction_detail = []

    try:
        for transaction_detail in transaction_details:
            check_and_update_stock(db, transaction_detail.product_id, transaction_detail.quantity_transaction)

            new_transaction_detail = TransactionDetail(
                transaction_detail_transaction=id_transaction,
                transaction_detail_product=transaction_detail.product_id,
                transaction_detail_quantity=transaction_detail.quantity_transaction,
                transaction_detail_price=transaction_detail.product_price,
                transaction_detail_subtotal=transaction_detail.quantity_transaction * transaction_detail.product_price
            )
            db_transaction_detail.append(new_transaction_detail)

        db.add_all(db_transaction_detail)
        db.commit()
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create transaction details")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

    return db_transaction_detail