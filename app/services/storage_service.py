from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile, HTTPException, status
import os
from fastapi.responses import FileResponse

class StorageService:

    STORAGE_DIR = Path("storage/documents")

    @classmethod
    async def save_file(
        cls,
        file: UploadFile
    ):

        extension = Path(file.filename).suffix

        stored_name = f"{uuid4()}{extension}"

        file_path = cls.STORAGE_DIR / stored_name

        content = await file.read()

        file_path.write_bytes(content)

        return {
            "stored_filename": stored_name,
            "original_filename": file.filename,
            "mime_type": file.content_type,
            "file_size": len(content),
            "file_path": file_path,
        }

    @classmethod
    def delete_file(
        cls,
        stored_filename: str
    ):

        file_path = cls.STORAGE_DIR / stored_filename

        if file_path.exists():
            file_path.unlink()

    
    @classmethod
    def get_file_path(cls, stored_filename: str) -> str:
        file_path = cls.STORAGE_DIR / stored_filename

        if not file_path.exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File not found on server.",
            )

        return str(file_path)