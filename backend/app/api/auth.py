from fastapi import APIRouter, Depends, status

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)

from app.services.auth_service import (
    AuthService
)

from app.core.dependencies import (
    get_auth_service
)
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(

    data: UserCreate,

    service: AuthService = Depends(
        get_auth_service
    )
):

    return service.register(
        data
    )

@router.post(
    "/login",
    response_model=Token
)
def login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    service: AuthService = Depends(
        get_auth_service
    )
):

    return service.login(
        email=form_data.username,
        password=form_data.password
    )