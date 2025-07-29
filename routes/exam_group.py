
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupResponse, ExamGroupCreate, ExamGroupUpdate
from http import HTTPStatus

from flask import Blueprint, request, Response
import json
from database import db
from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupResponseSchema, ExamGroupCreateSchema, ExamGroupUpdateSchema


exam_group_bp = Blueprint('exam_group_bp', __name__)


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


@exam_group_bp.route("/exam_groups_orm", methods=["GET"])
def get_exam_groups():
    session = SessionLocal()
    try:
        exam_groups = session.query(ExamGroup).all()
        result = [ExamGroupResponse.from_orm(eg).dict() for eg in exam_groups]
        return jsonify(result)
    finally:
        session.close()

@exam_group_bp.route("/exam_groups_orm/<string:group_code>", methods=["GET"])
def get_exam_group(group_code):
    session = SessionLocal()
    try:
        exam_group = session.query(ExamGroup).filter(ExamGroup.group_code == group_code).first()
        if not exam_group:
            return jsonify({"error": "Exam group not found"}), HTTPStatus.NOT_FOUND
        return jsonify(ExamGroupResponse.from_orm(exam_group).dict())
    finally:
        session.close()

@exam_group_bp.route("/exam_groups_orm", methods=["POST"])
def create_exam_group():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data or not data.get("group_code") or not data.get("description"):
            return jsonify({"error": "group_code and description are required"}), HTTPStatus.BAD_REQUEST
        
        # Kiểm tra xem group_code đã tồn tại chưa
        if session.query(ExamGroup).filter(ExamGroup.group_code == data["group_code"]).first():
            return jsonify({"error": "Exam group code already exists"}), HTTPStatus.CONFLICT
        
        exam_group = ExamGroup(
            group_code=data["group_code"],
            description=data["description"]
        )
        session.add(exam_group)
        session.commit()
        return jsonify(ExamGroupResponse.from_orm(exam_group).dict()), HTTPStatus.CREATED
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@exam_group_bp.route("/exam_groups_orm/<string:group_code>", methods=["PUT"])
def update_exam_group(group_code):
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST
        
        exam_group = session.query(ExamGroup).filter(ExamGroup.group_code == group_code).first()
        if not exam_group:
            return jsonify({"error": "Exam group not found"}), HTTPStatus.NOT_FOUND
        # Cập nhật trường được cung cấp
        if "description" in data:
            exam_group.description = data["description"]
        
        session.commit()
        return jsonify(ExamGroupResponse.from_orm(exam_group).dict())
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@exam_group_bp.route("/exam_groups_orm/<string:group_code>", methods=["DELETE"])
def delete_exam_group(group_code):
    session = SessionLocal()
    try:
        exam_group = session.query(ExamGroup).filter(ExamGroup.group_code == group_code).first()
        if not exam_group:
            return jsonify({"error": "Exam group not found"}), HTTPStatus.NOT_FOUND
        
        session.delete(exam_group)
        session.commit()
        return jsonify({"message": "Exam group deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

@exam_group_bp.route('/', methods=['GET'])
def get_exam_groups():
    groups = ExamGroup.query.all()
    data = ExamGroupResponseSchema(many=True).dump(groups)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@exam_group_bp.route('/<string:group_code>', methods=['GET'])
def get_exam_group(group_code):
    group = ExamGroup.query.get_or_404(group_code)
    data = ExamGroupResponseSchema().dump(group)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@exam_group_bp.route('/', methods=['POST'])
def create_exam_group():
    data = ExamGroupCreateSchema().load(request.json)
    group = ExamGroup(**data)
    db.session.add(group)
    db.session.commit()
    result = ExamGroupResponseSchema().dump(group)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@exam_group_bp.route('/<string:group_code>', methods=['PUT'])
def update_exam_group(group_code):
    group = ExamGroup.query.get_or_404(group_code)
    data = ExamGroupUpdateSchema().load(request.json)
    for key, value in data.items():
        setattr(group, key, value)
    db.session.commit()
    result = ExamGroupResponseSchema().dump(group)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@exam_group_bp.route('/<string:group_code>', methods=['DELETE'])
def delete_exam_group(group_code):
    group = ExamGroup.query.get_or_404(group_code)
    db.session.delete(group)
    db.session.commit()
    return '', 204

