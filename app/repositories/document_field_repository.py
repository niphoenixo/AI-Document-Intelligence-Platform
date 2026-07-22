from sqlalchemy.orm import Session

from app.models.document_field import DocumentField


class DocumentFieldRepository:

    @staticmethod
    def create(
        db: Session,
        document_id: int,
        invoice_number: str = None,
        vendor: str = None,
        amount: float = None,
        currency: str = None,
        invoice_date=None,
    ) -> DocumentField:

        document_field = DocumentField(
            document_id=document_id,
            invoice_number=invoice_number,
            vendor=vendor,
            amount=amount,
            currency=currency,
            invoice_date=invoice_date,
        )

        db.add(document_field)
        db.commit()
        db.refresh(document_field)

        return document_field

    @staticmethod
    def get_by_document_id(
        db: Session,
        document_id: int,
    ):
        return (
            db.query(DocumentField)
            .filter(DocumentField.document_id == document_id)
            .first()
        )