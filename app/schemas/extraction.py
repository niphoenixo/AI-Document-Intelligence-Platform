from datetime import date
from typing import Optional

from pydantic import BaseModel


class ExtractedFields(BaseModel):
    invoice_number: Optional[str] = None
    vendor: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    invoice_date: Optional[date] = None