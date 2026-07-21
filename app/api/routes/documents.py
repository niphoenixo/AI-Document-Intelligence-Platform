from fastapi import APIRouter, Depends, File, UploadFile, Query
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.document import (
    DocumentUploadResponse,
    DocumentResponse,
)
from app.services.document_service import DocumentService
from typing import List
from app.schemas.document import DocumentContentResponse

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


@router.get(
        "",
        response_model=List[DocumentResponse],
)

def get_documents(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return DocumentService.get_documents(
        db=db,
        current_user=current_user,
        page=page,
        size=size,
    )

@router.get(
    "/{document_uuid}",
    response_model=DocumentResponse,
)
def get_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return DocumentService.get_document(
        db=db,
        current_user=current_user,
        document_uuid=document_uuid,
    )

@router.delete("/{document_uuid}")
def delete_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return DocumentService.delete_document(
        db=db,
        current_user=current_user,
        document_uuid=document_uuid,
    )

@router.get("/{document_uuid}/download")
def download_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = DocumentService.download_document(
        db=db,
        current_user=current_user,
        document_uuid=document_uuid,
    )

    return FileResponse(
        path=result["file_path"],
        filename=result["filename"],
        media_type="application/octet-stream",
    )

@router.post(
    "/{document_uuid}/process",
)
def process_document(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return DocumentService.process_document(
        db=db,
        current_user=current_user,
        document_uuid=document_uuid,
    )

@router.get(
    "/{document_uuid}/content",
    response_model=DocumentContentResponse,
)
def get_document_content(
    document_uuid: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return DocumentService.get_document_content(
        db=db,
        current_user=current_user,
        document_uuid=document_uuid,
    )