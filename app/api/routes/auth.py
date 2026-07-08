from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.auth import RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        user = AuthService.register(
            db,
            request
        )

        return {
            "message": "User registered successfully.",
            "user_id": user.uuid
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )