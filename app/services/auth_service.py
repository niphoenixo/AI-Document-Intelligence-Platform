from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest
from app.utils.security import hash_password
from app.utils.security import (
    verify_password,
    create_access_token
)
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        request: RegisterRequest
    ):

        existing_user = UserRepository.get_by_email(
            db,
            request.email
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        user = User(
            full_name=request.full_name,
            email=request.email,
            password_hash=hash_password(
                request.password
            )
        )
       

        return UserRepository.create(
            db,
            user
        )
    
    @staticmethod
    def login(
        db: Session,
        request: LoginRequest
    ):

        user = UserRepository.get_by_email(
            db,
            request.email
        )

        if not user:
            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            request.password,
            user.password_hash
        ):
            raise ValueError(
                "Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }