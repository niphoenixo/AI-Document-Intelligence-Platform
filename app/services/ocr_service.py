from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class OCRService:
    
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract text from a PDF or image file.
        """

        file_extension = Path(file_path).suffix.lower()

        if file_extension == ".pdf":
            return OCRService._extract_from_pdf(file_path)

        return OCRService._extract_from_image(file_path)

    @staticmethod
    def _extract_from_pdf(file_path: str) -> str:
        """
        Convert each PDF page to an image and run OCR.
        """

        pages = convert_from_path(file_path)

        extracted_text = []

        for page in pages:
            text = pytesseract.image_to_string(page)

            if text.strip():
                extracted_text.append(text.strip())

        return "\n\n".join(extracted_text)

    @staticmethod
    def _extract_from_image(file_path: str) -> str:
        """
        Run OCR directly on an image.
        """

        image = Image.open(file_path)

        return pytesseract.image_to_string(image).strip()