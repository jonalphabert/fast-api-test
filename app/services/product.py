from sqlalchemy import text
from sqlalchemy.orm import Session
from app.schemas.product import ProductSchema

def get_product(db: Session):
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

def get_product_by_id(db: Session, product_id: int):
    sql = text("""
        SELECT 
            *
        FROM products
        WHERE product_id = :product_id
    """)

    result = db.execute(sql, {"product_id": product_id})

    product = result.fetchone()

    if product:
        return ProductSchema(
            product_id=product.product_id,
            product_barcode=product.product_barcode,
            product_name=product.product_name,
            product_price=product.product_price,
            product_quantity=product.product_quantity
        )
    return None

def update_stock(db: Session, product_id: int, amount):
    sql = text("""
        UPDATE
            products
        SET
            product_quantity = product_quantity - :amount
        WHERE
            product_id = :product_id
    """)

    result = db.execute(sql, {"product_id": product_id})