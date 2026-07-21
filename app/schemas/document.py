from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentUploadResponse(BaseModel):
    uuid: str
    original_filename: str
    status: str

class DocumentResponse(BaseModel):
    uuid: UUID
    original_filename: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DocumentContentResponse(BaseModel):
    raw_text: str
    page_count: int

    model_config = ConfigDict(from_attributes=True)
