from sqlalchemy.orm import Session

from app.models.document_content import DocumentContent


class DocumentContentRepository:

    @staticmethod
    def create(
        db: Session,
        document_id: int,
        raw_text: str,
        page_count: int = 1,
    ) -> DocumentContent:

        document_content = DocumentContent(
            document_id=document_id,
            raw_text=raw_text,
            page_count=page_count,
        )

        db.add(document_content)
        db.commit()
        db.refresh(document_content)

        return document_content

    @staticmethod
    def get_by_document_id(
        db: Session,
        document_id: int,
    ):
        return (
            db.query(DocumentContent)
            .filter(DocumentContent.document_id == document_id)
            .first()
        )
    
    @staticmethod
    def update(
        db: Session,
        document_content: DocumentContent,
        raw_text: str,
        page_count: int = 1,
    ) -> DocumentContent:

        document_content.raw_text = raw_text
        document_content.page_count = page_count

        db.commit()
        db.refresh(document_content)

        return document_content