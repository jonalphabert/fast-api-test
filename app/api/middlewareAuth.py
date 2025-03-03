from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwtGenerator import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    print(f"Token received: {token}")  # Debugging line

    # Replace this with your actual JWT verification function
    try:
        user = verify_access_token(token)
        return user
    except Exception as e:
        print(f"Token verification error: {e}")  # Debugging line
        raise HTTPException(status_code=401, detail="Invalid token")
