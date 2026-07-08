from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):

        stmt = (
            select(User)
            .where(User.email == email)
        )

        return db.scalar(stmt)

    @staticmethod
    def create(
        db: Session,
        user: User
    ):

        db.add(user)
        db.commit()
        db.refresh(user)

        return user