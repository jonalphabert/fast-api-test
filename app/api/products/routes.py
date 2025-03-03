from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import get_db
from app.services.product import get_product, get_product_by_id, get_product_by_codes, get_product_by_name
from app.schemas.product import ProductSchema
from app.api.middlewareAuth import get_current_user

router = APIRouter()

@router.get("/products", dependencies=[Depends(get_current_user)])
async def read_root(barcode: str = None, name: str = None, limit: int = 10, db: Session = Depends(get_db)):
    # barcode, name
    try:
        if barcode is not None:
            print(barcode)
            product = get_product_by_codes(db, barcode)
            if product is None:
                print("Product not found")
                raise HTTPException(status_code=404, detail="Product not found")
            return {
                "data": product
            }
        elif name is not None:
            product_list = get_product_by_name(db, name)

            if product_list is None:
                raise HTTPException(status_code=404, detail="Product not found")
            print(f"Product not found {product_list}")
            return {
                "data": product_list
            }

        product_list = get_product(db)
        return {"data": product_list}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@router.get("/products/{product_id}", dependencies=[Depends(get_current_user)])
async def read_product(product_id: int, db: Session = Depends(get_db)) -> ProductSchema:
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product