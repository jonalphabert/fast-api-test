from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.users import UserLoginRequest
from app.schemas.token import Token
from app.models import User
from app.databases import get_db
from sqlalchemy.orm import Session

from app.utils.hashlib import verify_password
from app.utils.jwtGenerator import create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(loginInfo: UserLoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == loginInfo.email).first()

    if not user or not verify_password(loginInfo.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create a JWT token
    access_token = create_access_token(data={"sub": user.email, "user_id": user.user_id, "name": user.name})
    return {"access_token": access_token, "token_type": "bearer"}