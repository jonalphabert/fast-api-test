from sqlalchemy import text
from sqlalchemy.orm import Session
# from app.schemas.transaction import TransactionSchema

def get_transactions(db: Session):
    sql = text("""
        SELECT 
            *
        FROM products
    """)

    result = db.execute(sql)
    products = result.fetchall()

    products_dict = [
        ProductSchema(
            product_id=row.product_id,
            product_barcode=row.product_barcode,
            product_name=row.product_name,
            product_price=row.product_price,
            product_quantity=row.product_quantity
        )
        for row in products
    ]

    return products_dict

def get_transaction_by_id(db: Session, product_id: int):
    # Define the raw SQL query
    sql = text("""
        SELECT 
            *
        FROM products
        WHERE product_id = :product_id
    """)

    # Execute the query with parameters
    result = db.execute(sql, {"product_id": product_id})  # Fix: Pass a dictionary

    # Fetch the first (and only) result
    product = result.fetchone()

    if product:
        # Convert the result into a dictionary
        return ProductSchema(
            product_id=product.product_id,
            product_barcode=product.product_barcode,
            product_name=product.product_name,
            product_price=product.product_price,
            product_quantity=product.product_quantity
        )
    return None  # Return None if no product is found