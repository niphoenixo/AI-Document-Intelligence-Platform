from sqlalchemy.orm import Session

from app.repositories.document_content_repository import (
    DocumentContentRepository,
)

class DocumentContentService:

    @staticmethod
    def save_content(
        db: Session,
        document_id: int,
        raw_text: str,
        page_count: int = 1,
    ):

        # Check if OCR content already exists
        existing_content = DocumentContentRepository.get_by_document_id(
            db=db,
            document_id=document_id,
        )

        # Update existing record
        if existing_content:
            return DocumentContentRepository.update(
                db=db,
                document_content=existing_content,
                raw_text=raw_text,
                page_count=page_count,
            )

        # Otherwise create a new record
        return DocumentContentRepository.create(
            db=db,
            document_id=document_id,
            raw_text=raw_text,
            page_count=page_count,
        )
    
    @staticmethod
    def get_content(
        db: Session,
        document_id: int,
    ):
        return DocumentContentRepository.get_by_document_id(
            db=db,
            document_id=document_id,
        )