from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "gym-secret-key"
ALGORITHM = "HS256"


def authenticate_user(username: str, password: str):

    if username == "admin" and password == "admin123":
        return {"username": username}

    return None


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )