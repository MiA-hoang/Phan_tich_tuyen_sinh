from flask import Blueprint, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from models.university import University
from schemas.university import UniversityResponse

university_bp = Blueprint("university", __name__)

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

@university_bp.route("/universities", methods=["GET"])
def get_universities():
    session = SessionLocal()
    try:
        universities = session.query(University).all()
        result = [UniversityResponse.from_orm(u).dict() for u in universities]
        return jsonify(result)
    finally:
        session.close()