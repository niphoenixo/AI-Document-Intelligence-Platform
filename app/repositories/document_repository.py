from sqlalchemy.orm import Session

from app.models.document import Document

from app.models.document_status import DocumentStatus


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        document: Document
    ):

        db.add(document)

        db.commit()

        db.refresh(document)

        return document

    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id: int,
        page: int,
        size: int,
    ):
        return (
            db.query(Document)
            .filter(Document.uploaded_by == user_id)
            .order_by(Document.created_at.desc())
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )
    
    @staticmethod
    def get_by_uuid(
        db: Session,
        uuid: str,
    ):
        return (
            db.query(Document)
            .filter(Document.uuid == uuid)
            .first()
        )
    
    @staticmethod
    def delete(
        db: Session,
        document: Document,
    ):
        db.delete(document)
        db.commit()



    @staticmethod
    def update_status(
        db: Session,
        document: Document,
        status: DocumentStatus,
    ):
        document.status = status
        db.commit()
        db.refresh(document)

        return document