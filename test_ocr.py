from app.services.ocr_service import OCRService

file_path = "storage/documents/ff07c2cf-eb8a-41b5-9de3-d60c388b3473.pdf"


text = OCRService.extract_text(file_path)

print(text)