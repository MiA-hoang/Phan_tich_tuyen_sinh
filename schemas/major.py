from pydantic import BaseModel

class MajorResponse(BaseModel):
    major_id: str
    name: str
    field: str | None = None

    class Config:
        orm_mode = True