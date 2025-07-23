import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, String, Text
from database import Base

class ExamGroup(Base):
    __tablename__ = "EXAM_GROUPS"

    group_code = Column(String, primary_key=True)
    description = Column(Text)