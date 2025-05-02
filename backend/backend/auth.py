from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "super-secret-key"  # Replace with os.environ["JWT_SECRET"] in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "demo@user.com": {
        "id": 1,
        "email": "demo@user.com",
        "is_active": True,
    }
}

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return fake_users_db.get(email)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user or not user["is_active"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
