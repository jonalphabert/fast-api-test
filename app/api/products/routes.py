from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import get_db
from app.services.product import get_product, get_product_by_id
from app.schemas.product import ProductSchema

router = APIRouter()

@router.get("/products")
async def read_root(db: Session = Depends(get_db)):
    product_list = get_product(db)
    return {"message": "Hello, from products!", "data": product_list}

@router.get("/products/{product_id}")
async def read_product(product_id: int, db: Session = Depends(get_db)) -> ProductSchema:
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product