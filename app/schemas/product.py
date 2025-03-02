from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_id      : int
    product_barcode : str
    product_name    : str
    product_price   : float
    product_quantity: int

class ProductNotFoundSchema(BaseModel):
    status: int = 404
    detail: str
