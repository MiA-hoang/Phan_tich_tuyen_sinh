
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from database import Base

class AdmissionData(Base):
    __tablename__ = "ADMISSION_SCORES"

    data_id = Column(Integer, primary_key=True, autoincrement=True)  
    university_id = Column(String, ForeignKey("universities.id"))     
    major_id = Column(String, ForeignKey("majors.major_id"))          
    group_code = Column(String, ForeignKey("exam_groups.group_code"))

    year = Column(Integer)
    min_score = Column(Float)
    quota = Column(Integer)
    note = Column(String)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
