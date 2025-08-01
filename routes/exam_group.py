from flask import Blueprint, request, Response
import json
from database import db
from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupResponseSchema, ExamGroupCreateSchema, ExamGroupUpdateSchema

exam_group_bp = Blueprint('exam_group_bp', __name__, url_prefix="/api/exam-groups")

@exam_group_bp.route("/", methods=["GET"])
def get_exam_groups():
    groups = ExamGroup.query.all()
    data = ExamGroupResponseSchema(many=True).dump(groups)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@exam_group_bp.route("/", methods=["POST"])
def create_exam_group():
    data = ExamGroupCreateSchema().load(request.json)
    group = ExamGroup(**data)
    db.session.add(group)
    db.session.commit()
    result = ExamGroupResponseSchema().dump(group)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@exam_group_bp.route("/<string:group_code>", methods=["PUT"])
def update_exam_group(group_code):
    group = ExamGroup.query.get_or_404(group_code)
    data = ExamGroupUpdateSchema().load(request.json)
    for key, value in data.items():
        setattr(group, key, value)
    db.session.commit()
    result = ExamGroupResponseSchema().dump(group)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@exam_group_bp.route("/<string:group_code>", methods=["DELETE"])
def delete_exam_group(group_code):
    group = ExamGroup.query.get_or_404(group_code)
    db.session.delete(group)
    db.session.commit()
    return "", 204
