from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserLoginRequest(BaseModel):
    email: str
    password: str
