from flask import Blueprint, request, Response
import json
from database import db
from models.major import Major
from schemas.major import MajorResponseSchema, MajorCreateSchema, MajorUpdateSchema

major_bp = Blueprint('major_bp', __name__, url_prefix="/api/majors")

@major_bp.route("/", methods=["GET"])
def get_majors():
    majors = Major.query.all()
    data = MajorResponseSchema(many=True).dump(majors)
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
    return "", 204
