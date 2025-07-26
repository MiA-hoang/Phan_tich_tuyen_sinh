from sqlalchemy import Column, String, Text
from database import Base

class University(Base):
    __tablename__ = "UNIVERSITIES"

    university_id = Column(String, primary_key=True)
    name = Column(Text, nullable=False)
    university_type = Column(Text)
    city = Column(Text)
    region = Column(Text)