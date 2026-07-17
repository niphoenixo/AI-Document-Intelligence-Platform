from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/api/v1/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    document = await DocumentService.upload_document(
        db,
        current_user,
        file,
    )

    return DocumentUploadResponse(
        uuid=document.uuid,
        original_filename=document.original_filename,
        status=document.status,
    )