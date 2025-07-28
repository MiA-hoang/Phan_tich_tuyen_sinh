from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from models.admission_data import AdmissionData
from schemas.admission_data import AdmissionDataResponse, AdmissionDataCreate, AdmissionDataUpdate
from http import HTTPStatus
from datetime import datetime

admission_data_bp = Blueprint("admission_data", __name__)

connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=NGOCHA;"
    "Database=DuAn BIT;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string),
    echo=True
)

SessionLocal = sessionmaker(bind=engine)

@admission_data_bp.route("/admission_scores", methods=["GET"])
def get_admission_scores():
    session = SessionLocal()
    try:
        admission_scores = session.query(AdmissionData).all()
        result = [AdmissionDataResponse.from_orm(ad).dict() for ad in admission_scores]
        return jsonify(result)
    finally:
        session.close()

@admission_data_bp.route("/admission_scores/<int:data_id>", methods=["GET"])
def get_admission_score(data_id):
    session = SessionLocal()
    try:
        admission_score = session.query(AdmissionData).filter(AdmissionData.data_id == data_id).first()
        if not admission_score:
            return jsonify({"error": "Admission score not found"}), HTTPStatus.NOT_FOUND
        return jsonify(AdmissionDataResponse.from_orm(admission_score).dict())
    finally:
        session.close()

@admission_data_bp.route("/admission_scores", methods=["POST"])
def create_admission_score():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["university_id", "major_id", "group_code", "year"]):
            return jsonify({"error": "university_id, major_id, group_code, and year are required"}), HTTPStatus.BAD_REQUEST
        
        # Kiểm tra xem tổ hợp university_id, major_id, group_code, year đã tồn tại chưa
        if session.query(AdmissionData).filter(
            AdmissionData.university_id == data["university_id"],
            AdmissionData.major_id == data["major_id"],
            AdmissionData.group_code == data["group_code"],
            AdmissionData.year == data["year"]
        ).first():
            return jsonify({"error": "Admission score for this combination already exists"}), HTTPStatus.CONFLICT
        
        admission_score = AdmissionData(
            university_id=data["university_id"],
            major_id=data["major_id"],
            group_code=data["group_code"],
            year=data["year"],
            min_score=data.get("min_score"),
            quota=data.get("quota"),
            note=data.get("note"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        session.add(admission_score)
        session.commit()
        return jsonify(AdmissionDataResponse.from_orm(admission_score).dict()), HTTPStatus.CREATED
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@admission_data_bp.route("/admission_scores/<int:data_id>", methods=["PUT"])
def update_admission_score(data_id):
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST
        
        admission_score = session.query(AdmissionData).filter(AdmissionData.data_id == data_id).first()
        if not admission_score:
            return jsonify({"error": "Admission score not found"}), HTTPStatus.NOT_FOUND
        
        # Cập nhật các trường được cung cấp
        if "min_score" in data:
            admission_score.min_score = data["min_score"]
        if "quota" in data:
            admission_score.quota = data["quota"]
        if "note" in data:
            admission_score.note = data["note"]
        admission_score.updated_at = datetime.utcnow()
        
        session.commit()
        return jsonify(AdmissionDataResponse.from_orm(admission_score).dict())
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@admission_data_bp.route("/admission_scores/<int:data_id>", methods=["DELETE"])
def delete_admission_score(data_id):
    session = SessionLocal()
    try:
        admission_score = session.query(AdmissionData).filter(AdmissionData.data_id == data_id).first()
        if not admission_score:
            return jsonify({"error": "Admission score not found"}), HTTPStatus.NOT_FOUND
        
        session.delete(admission_score)
        session.commit()
        return jsonify({"message": "Admission score deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()