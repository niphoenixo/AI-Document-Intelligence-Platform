from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import DocumentRepository
from app.services.file_validation_service import FileValidationService
from app.services.storage_service import StorageService


class DocumentService:

    @staticmethod
    async def upload_document(
        db: Session,
        current_user: User,
        file: UploadFile,
    ):

        # Step 1: Validate
        await FileValidationService.validate(file)

        # Step 2: Save file
        file_info = await StorageService.save_file(file)

        try:

            # Step 3: Create document object
            document = Document(
                original_filename=file_info["original_filename"],
                stored_filename=file_info["stored_filename"],
                mime_type=file_info["mime_type"],
                file_size=file_info["file_size"],
                uploaded_by=current_user.id,
            )

            # Step 4: Save metadata
            return DocumentRepository.create(
                db,
                document,
            )

        except Exception as e:

            # Rollback database transaction
            db.rollback()

            # Delete uploaded file
            StorageService.delete_file(
                file_info["stored_filename"]
            )

            raise HTTPException(
                status_code=500,
                detail="Failed to upload document."
            ) from e