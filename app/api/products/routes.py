from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import get_db
from app.services.product import get_product, get_product_by_id
from app.schemas.product import ProductSchema
from app.api.middlewareAuth import get_current_user

router = APIRouter()

@router.get("/products", dependencies=[Depends(get_current_user)])
async def read_root(db: Session = Depends(get_db)):
    product_list = get_product(db)
    return {"message": "Hello, from products!", "data": product_list}

@router.get("/products/{product_id}", dependencies=[Depends(get_current_user)])
async def read_product(product_id: int, db: Session = Depends(get_db)) -> ProductSchema:
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product