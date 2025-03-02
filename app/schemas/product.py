from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str

class ProductNotFoundSchema(BaseModel):
    status: int = 404
    detail: str
