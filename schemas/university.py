from pydantic import BaseModel

class UniversityResponse(BaseModel):
    university_id: str
    name: str
    university_type: str | None = None
    city: str | None = None
    region: str | None = None

    class Config:
        orm_mode = True