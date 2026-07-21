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