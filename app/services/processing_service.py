import time
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_status import DocumentStatus
from app.repositories.document_repository import DocumentRepository
from app.services.document_content_service import DocumentContentService

from app.services.extraction_service import ExtractionService
from app.services.document_field_service import DocumentFieldService
from pathlib import Path
from app.services.ocr_service import OCRService

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

            extraction_service = ExtractionService()
            fields = extraction_service.extract_fields(raw_text)

            DocumentFieldService.save_fields(
                db=db,
                document_id=document.id,
                fields=fields,
            )

            DocumentRepository.update_status(
                db=db,
                document=document,
                status=DocumentStatus.COMPLETED.value,
            )

        except Exception:

            db.rollback()

            DocumentRepository.update_status(
                db=db,
                document=document,
                status=DocumentStatus.FAILED.value,
            )

            raise

    @staticmethod
    def extract_text(
        document: Document,
    ) -> str:

        file_path = Path("storage") / "documents" / document.stored_filename

        return OCRService.extract_text(str(file_path))

    @staticmethod
    def _extract_fields(
        document: Document,
    ):
        time.sleep(3)

   