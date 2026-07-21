import time
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_status import DocumentStatus
from app.repositories.document_repository import DocumentRepository
from app.services.document_content_service import DocumentContentService

class ProcessingService:

    @staticmethod
    def process_document(
        db: Session,
        document: Document,
    ):
        try:
            DocumentRepository.update_status(
                db=db,
                document=document,
                status=DocumentStatus.PROCESSING.value,
            )

            raw_text = ProcessingService.extract_text(document)

            DocumentContentService.save_content(
                db=db,
                document_id=document.id,
                raw_text=raw_text,
            )

            ProcessingService.extract_fields(document)

            DocumentRepository.update_status(
                db=db,
                document=document,
                status=DocumentStatus.COMPLETED.value,
            )

        except Exception:

            DocumentRepository.update_status(
                db=db,
                document=document,
                status=DocumentStatus.FAILED.value,
            )

            raise

    @staticmethod
    def extract_text(
        document: Document,
    ):
        time.sleep(2)

        return """
        Invoice Number: INV-1001

        Vendor: Amazon UK

        Amount: £425

        Date: 20/07/2026
        """

    @staticmethod
    def extract_fields(
        document: Document,
    ):
        time.sleep(3)