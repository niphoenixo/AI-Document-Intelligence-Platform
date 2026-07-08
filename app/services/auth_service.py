from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest
from app.utils.security import hash_password


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