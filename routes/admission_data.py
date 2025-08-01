from flask import Blueprint, request, Response
import json
from database import db
from models.admission_data import AdmissionScore
from schemas.admission_data import AdmissionScoreResponseSchema, AdmissionScoreCreateSchema, AdmissionScoreUpdateSchema

admission_data_bp = Blueprint('admission_data_bp', __name__, url_prefix="/api/admission-scores")

@admission_data_bp.route("/", methods=["GET"])
def get_scores():
    scores = AdmissionScore.query.all()
    data = AdmissionScoreResponseSchema(many=True).dump(scores)
    return Response(json.dumps(data, ensure_ascii=False), mimetype="application/json")

@admission_data_bp.route("/", methods=["POST"])
def create_score():
    data = AdmissionScoreCreateSchema().load(request.json)
    score = AdmissionScore(**data)
    db.session.add(score)
    db.session.commit()
    result = AdmissionScoreResponseSchema().dump(score)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json"), 201

@admission_data_bp.route("/<int:id>", methods=["PUT"])
def update_score(id):
    score = AdmissionScore.query.get_or_404(id)
    data = AdmissionScoreUpdateSchema().load(request.json)
    for key, value in data.items():
        setattr(score, key, value)
    db.session.commit()
    result = AdmissionScoreResponseSchema().dump(score)
    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@admission_data_bp.route("/<int:id>", methods=["DELETE"])
def delete_score(id):
    score = AdmissionScore.query.get_or_404(id)
    db.session.delete(score)
    db.session.commit()
    return "", 204
