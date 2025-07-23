from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AdmissionDataCreate(BaseModel):
    university_id: str
    major_id: str
    group_code: str
    year: int
    min_score: Optional[float] = None
    quota: Optional[int] = None
    note: Optional[str] = None

class AdmissionDataUpdate(BaseModel):
    min_score: Optional[float] = None
    quota: Optional[int] = None
    note: Optional[str] = None

class AdmissionDataResponse(AdmissionDataCreate):
    data_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True