from sqlalchemy import text
from sqlalchemy.orm import Session
from app.schemas.product import ProductSchema
from sqlalchemy.exc import SQLAlchemyError

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

def check_and_update_stock(db: Session, product_id: int, quantity: int):
    try:
        product = db.query(Product).filter(Product.product_id == product_id).with_for_update().one()

        if product.product_quantity < quantity:
            raise ValueError(f"Insufficient stock for product {product_id}")

        product.product_quantity -= quantity

        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update product stock")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred")