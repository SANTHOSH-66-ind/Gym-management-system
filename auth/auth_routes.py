from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.auth_service import (
    authenticate_user,
    create_access_token
)

router = APIRouter()


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    access_token = create_access_token(
        {"sub": user["username"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }