from sqlalchemy.orm import Session

from app.repositories.document_field_repository import (
    DocumentFieldRepository,
)
from app.schemas.extraction import ExtractedFields

class DocumentFieldService:

    @staticmethod
    def save_fields(
        db: Session,
        document_id: int,
        fields: ExtractedFields,
    ):
        return DocumentFieldRepository.create(
            db=db,
            document_id=document_id,
            invoice_number=fields.invoice_number,
            vendor=fields.vendor,
            amount=fields.amount,
            currency=fields.currency,
            invoice_date=fields.invoice_date,
        )

    @staticmethod
    def get_fields(
        db: Session,
        document_id: int,
    ):
        return DocumentFieldRepository.get_by_document_id(
            db=db,
            document_id=document_id,
        )