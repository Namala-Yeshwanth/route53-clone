from app.models.user import User

from app.repositories.user_repository import (
    UserRepository
)

from app.schemas.user import (
    UserCreate
)

from app.security.hashing import (
    hash_password,
    verify_password
)

from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException
)

from app.security.jwt import (
    create_access_token
)


class AuthService:

    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    def register(
        self,
        data: UserCreate
    ):

        existing_user = (
            self.repository.get_by_email(
                data.email
            )
        )

        if existing_user:
            raise UserAlreadyExistsException()

        user = User(
            name=data.name,
            email=data.email,
            password_hash=hash_password(
                data.password
            )
        )

        return self.repository.create(
            user
        )
    
    def login(
        self,
        email: str,
        password: str
    ):

        user = self.repository.get_by_email(
            email
        )

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(
            password,
            user.password_hash
        ):
            raise InvalidCredentialsException()

        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }