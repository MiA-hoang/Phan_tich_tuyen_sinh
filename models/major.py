from sqlalchemy import Column, String, Text
from database import Base

class Major(Base):
    __tablename__ = "MAJORS"

    major_id = Column(String, primary_key=True)
    name = Column(Text, nullable=False)
    field = Column(Text)