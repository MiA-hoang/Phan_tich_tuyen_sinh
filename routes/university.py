
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from models.university import University
from schemas.university import UniversityResponse
from http import HTTPStatus

from flask import Blueprint, request, Response
import json
from database import db
from models.university import University
from schemas.university import UniversityResponseSchema, UniversityCreateSchema, UniversityUpdateSchema


university_bp = Blueprint('university_bp', __name__)


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

@university_bp.route("/universities", methods=["GET"])
def get_universities():
    session = SessionLocal()
    try:
        universities = session.query(University).all()
        result = [UniversityResponse.from_orm(u).dict() for u in universities]
        return jsonify(result)
    finally:
        session.close()

@university_bp.route("/universities/<string:university_id>", methods=["GET"])
def get_university(university_id):
    session = SessionLocal()
    try:
        university = session.query(University).filter(University.university_id == university_id).first()
        if not university:
            return jsonify({"error": "University not found"}), HTTPStatus.NOT_FOUND
        return jsonify(UniversityResponse.from_orm(university).dict())
    finally:
        session.close()

@university_bp.route("/universities", methods=["POST"])
def create_university():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data or not data.get("university_id") or not data.get("name"):
            return jsonify({"error": "university_id and name are required"}), HTTPStatus.BAD_REQUEST
        
        # Kiểm tra xem university_id đã tồn tại chưa
        if session.query(University).filter(University.university_id == data["university_id"]).first():
            return jsonify({"error": "University ID already exists"}), HTTPStatus.CONFLICT
        
        university = University(
            university_id=data["university_id"],
            name=data["name"],
            university_type=data.get("university_type"),
            city=data.get("city"),
            region=data.get("region")
        )
        session.add(university)
        session.commit()
        return jsonify(UniversityResponse.from_orm(university).dict()), HTTPStatus.CREATED
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@university_bp.route("/universities/<string:university_id>", methods=["PUT"])
def update_university(university_id):
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST
        
        university = session.query(University).filter(University.university_id == university_id).first()
        if not university:
            return jsonify({"error": "University not found"}), HTTPStatus.NOT_FOUND
        
        # Cập nhật các trường được cung cấp
        if "name" in data:
            university.name = data["name"]
        if "university_type" in data:
            university.university_type = data["university_type"]
        if "city" in data:
            university.city = data["city"]
        if "region" in data:
            university.region = data["region"]
        
        session.commit()
        return jsonify(UniversityResponse.from_orm(university).dict())
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@university_bp.route("/universities/<string:university_id>", methods=["DELETE"])
def delete_university(university_id):
    session = SessionLocal()
    try:
        university = session.query(University).filter(University.university_id == university_id).first()
        if not university:
            return jsonify({"error": "University not found"}), HTTPStatus.NOT_FOUND
        
        session.delete(university)
        session.commit()
        return jsonify({"message": "University deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@university_bp.route("/", methods=["GET"])
def get_universities():
    universities = University.query.all()
    data = UniversityResponseSchema(many=True).dump(universities)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@university_bp.route("/", methods=["POST"])
def create_university():
    data = UniversityCreateSchema().load(request.json)
    university = University(**data)
    db.session.add(university)
    db.session.commit()
    result = UniversityResponseSchema().dump(university)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@university_bp.route("/<string:university_id>", methods=["PUT"])
def update_university(university_id):
    university = University.query.get_or_404(university_id)
    data = UniversityUpdateSchema().load(request.json)
    for key, value in data.items():
        setattr(university, key, value)
    db.session.commit()
    result = UniversityResponseSchema().dump(university)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@university_bp.route("/<string:university_id>", methods=["DELETE"])
def delete_university(university_id):
    university = University.query.get_or_404(university_id)
    db.session.delete(university)
    db.session.commit()
    return "", 204

