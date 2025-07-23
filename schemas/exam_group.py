from pydantic import BaseModel
from typing import Optional

class ExamGroupCreate(BaseModel):
    group_code: str
    description: str  

class ExamGroupUpdate(BaseModel):
    description: Optional[str] = None  

class ExamGroupResponse(ExamGroupCreate):
    class Config:
        from_attributes = True