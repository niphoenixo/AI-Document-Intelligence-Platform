from datetime import date
from app.schemas.extraction import ExtractedFields
class ExtractionService:

    @staticmethod
    def extract_fields(raw_text: str) -> ExtractedFields:

        return ExtractedFields(
            invoice_number="INV-1001",
            vendor="Amazon UK",
            amount=425.0,
            currency="GBP",
            invoice_date=date(2026, 7, 20),
        )