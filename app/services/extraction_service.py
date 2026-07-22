from datetime import date
from app.schemas.extraction import ExtractedFields
from app.services.llm_service import LLMService


class ExtractionService:

    def __init__(self):
        self.llm_service = LLMService()

    @staticmethod
    def build_prompt(ocr_text: str) -> str:
        return f"""
You are an intelligent document extraction assistant.

Extract the following fields from the document.

Return ONLY valid JSON.

Schema:
{{
    "invoice_number": string | null,
    "vendor": string | null,
    "amount": number | null,
    "currency": string | null,
    "invoice_date": "YYYY-MM-DD" | null
}}

Rules:
- Do not include explanations.
- If a field is missing, return null.
- Amount should be numeric only.
- Currency should be the ISO currency code if possible.
- Return only valid JSON.

Document Text:
-----------------------
{ocr_text}
-----------------------
"""

    def extract_fields(self, ocr_text: str) -> ExtractedFields:

        prompt = self.build_prompt(ocr_text)

        # TODO: Enable after configuring a valid OpenAI API key
        # response = self.llm_service.ask(prompt)
        # data = json.loads(response)
        # return ExtractedFields(**data)

        prompt = self.build_prompt(ocr_text)

        # ===== Future implementation =====
        #
        # response = self.llm_service.ask(prompt)
        #
        # data = json.loads(response)
        #
        # return ExtractedFields(**data)
        #
        # ================================

        # Temporary placeholder
        return ExtractedFields(
            invoice_number="INV-1001",
            vendor="Amazon UK",
            amount=425.0,
            currency="GBP",
            invoice_date="2026-07-20",
        )