from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User

from app.repositories.document_repository import DocumentRepository

from app.services.storage_service import StorageService
from app.services.file_validation_service import FileValidationService


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
        
    @staticmethod
    def get_documents(
        db: Session,
        current_user: User,
        page: int,
        size: int,
    ):
        return DocumentRepository.get_all_by_user(
            db=db,
            user_id=current_user.id,
            page=page,
            size=size,
        )

    @staticmethod
    def get_document(
        db: Session,
        current_user: User,
        document_uuid: str,
    ):
        document = DocumentRepository.get_by_uuid(
            db=db,
            uuid=document_uuid,
        )

        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found."
            )

        if document.uploaded_by != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to access this document."
            )

        return document
    


    @staticmethod
    def delete_document(
        db: Session,
        current_user: User,
        document_uuid: str,
    ):
        document = DocumentRepository.get_by_uuid(
            db=db,
            uuid=document_uuid,
        )

        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found.",
            )

        if document.uploaded_by != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to delete this document.",
            )

        StorageService.delete_file(
            document.stored_filename,
        )

        DocumentRepository.delete(
            db=db,
            document=document,
        )

        return {
            "message": "Document deleted successfully."
        }


    @staticmethod
    def download_document(
        db: Session,
        current_user: User,
        document_uuid: str,
    ):
        document = DocumentRepository.get_by_uuid(
            db=db,
            uuid=document_uuid,
        )

        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found.",
            )

        if document.uploaded_by != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to access this document.",
            )

        file_path = StorageService.get_file_path(
            document.stored_filename,
        )

        return {
            "file_path": file_path,
            "filename": document.original_filename,
        }