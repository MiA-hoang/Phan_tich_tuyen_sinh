
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

from models.major import Major
from schemas.major import MajorResponse
from http import HTTPStatus

from flask import Blueprint, request, Response
import json
from database import db
from models.major import Major
from schemas.major import MajorResponseSchema, MajorCreateSchema, MajorUpdateSchema


major_bp = Blueprint('major_bp', __name__)


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

@major_bp.route("/majors", methods=["GET"])
def get_majors():
    session = SessionLocal()
    try:
        majors = session.query(Major).all()
        result = [MajorResponse.from_orm(m).dict() for m in majors]
        return jsonify(result)
    finally:
        session.close()

@major_bp.route("/majors/<string:major_id>", methods=["GET"])
def get_major(major_id):
    session = SessionLocal()
    try:
        major = session.query(Major).filter(Major.major_id == major_id).first()
        if not major:
            return jsonify({"error": "Major not found"}), HTTPStatus.NOT_FOUND
        return jsonify(MajorResponse.from_orm(major).dict())
    finally:
        session.close()

@major_bp.route("/majors", methods=["POST"])
def create_major():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data or not data.get("major_id") or not data.get("name"):
            return jsonify({"error": "major_id and name are required"}), HTTPStatus.BAD_REQUEST
        
        # Kiểm tra xem major_id đã tồn tại chưa
        if session.query(Major).filter(Major.major_id == data["major_id"]).first():
            return jsonify({"error": "Major ID already exists"}), HTTPStatus.CONFLICT
        
        major = Major(
            major_id=data["major_id"],
            name=data["name"],
            field=data.get("field")
        )
        session.add(major)
        session.commit()
        return jsonify(MajorResponse.from_orm(major).dict()), HTTPStatus.CREATED
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@major_bp.route("/majors/<string:major_id>", methods=["PUT"])
def update_major(major_id):
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST
        
        major = session.query(Major).filter(Major.major_id == major_id).first()
        if not major:
            return jsonify({"error": "Major not found"}), HTTPStatus.NOT_FOUND
        
        # Cập nhật các trường được cung cấp
        if "name" in data:
            major.name = data["name"]
        if "field" in data:
            major.field = data["field"]
        
        session.commit()
        return jsonify(MajorResponse.from_orm(major).dict())
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@major_bp.route("/majors/<string:major_id>", methods=["DELETE"])
def delete_major(major_id):
    session = SessionLocal()
    try:
        major = session.query(Major).filter(Major.major_id == major_id).first()
        if not major:
            return jsonify({"error": "Major not found"}), HTTPStatus.NOT_FOUND
        
        session.delete(major)
        session.commit()
        return jsonify({"message": "Major deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@major_bp.route("/", methods=["GET"])
def get_majors():
    majors = Major.query.all()
    data = MajorResponseSchema(many=True).dump(majors)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@major_bp.route("/<string:major_id>", methods=["GET"])
def get_major(major_id):
    major = Major.query.get_or_404(major_id)
    data = MajorResponseSchema().dump(major)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@major_bp.route("/", methods=["POST"])
def create_major():
    data = MajorCreateSchema().load(request.json)
    major = Major(**data)
    db.session.add(major)
    db.session.commit()
    result = MajorResponseSchema().dump(major)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@major_bp.route("/<string:major_id>", methods=["PUT"])
def update_major(major_id):
    major = Major.query.get_or_404(major_id)
    data = MajorUpdateSchema().load(request.json)
    for key, value in data.items():
        setattr(major, key, value)
    db.session.commit()
    result = MajorResponseSchema().dump(major)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@major_bp.route("/<string:major_id>", methods=["DELETE"])
def delete_major(major_id):
    major = Major.query.get_or_404(major_id)
    db.session.delete(major)
    db.session.commit()
    return '', 204

