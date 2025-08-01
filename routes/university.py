from flask import Blueprint, request, Response
from database import db
from models.university import University
from schemas.university import UniversityCreateSchema, UniversityUpdateSchema, UniversityResponseSchema
import json

university_bp = Blueprint("university", __name__, url_prefix="/api/universities")

@university_bp.route("/", methods=["POST"])
def create_university():
    data = UniversityCreateSchema().load(request.json)
    university = University(**data)
    db.session.add(university)
    db.session.commit()
    result = UniversityResponseSchema().dump(university)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@university_bp.route("/", methods=["GET"])
def get_universities():
    universities = University.query.all()
    result = UniversityResponseSchema(many=True).dump(universities)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@university_bp.route("/<string:university_id>", methods=["GET"])
def get_university(university_id):
    university = University.query.get_or_404(university_id)
    result = UniversityResponseSchema().dump(university)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@university_bp.route("/<string:university_id>", methods=["PUT"])
def update_university(university_id):
    university = University.query.get_or_404(university_id)
    update_data = UniversityUpdateSchema().load(request.json)
    for key, value in update_data.items():
        setattr(university, key, value)
    db.session.commit()
    result = UniversityResponseSchema().dump(university)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@university_bp.route("/<string:university_id>", methods=["DELETE"])
def delete_university(university_id):
    university = University.query.get_or_404(university_id)
    db.session.delete(university)
    db.session.commit()
    return Response(json.dumps({"message": "Deleted successfully"}, ensure_ascii=False), mimetype="application/json")
