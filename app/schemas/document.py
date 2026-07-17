from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    uuid: str
    original_filename: str
    status: str