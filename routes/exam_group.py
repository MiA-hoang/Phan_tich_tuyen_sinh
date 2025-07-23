from flask import Blueprint, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus  # thêm để encode connection string

from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupResponse

exam_group_bp = Blueprint("exam_group", __name__)


connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-9C1G29S;"
    "Database=DuAn BIT;"
    "Trusted_Connection=yes;"
)


engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string),
    echo=True
)


SessionLocal = sessionmaker(bind=engine)


@exam_group_bp.route("/exam_groups_orm", methods=["GET"])
def get_exam_groups():
    session = SessionLocal()
    try:
        exam_groups = session.query(ExamGroup).all()
        result = [ExamGroupResponse.from_orm(eg).dict() for eg in exam_groups]
        return jsonify(result)
    finally:
        session.close()