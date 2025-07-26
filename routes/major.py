from flask import Blueprint, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from models.major import Major
from schemas.major import MajorResponse

major_bp = Blueprint("major", __name__)

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

@major_bp.route("/majors", methods=["GET"])
def get_majors():
    session = SessionLocal()
    try:
        majors = session.query(Major).all()
        result = [MajorResponse.from_orm(m).dict() for m in majors]
        return jsonify(result)
    finally:
        session.close()