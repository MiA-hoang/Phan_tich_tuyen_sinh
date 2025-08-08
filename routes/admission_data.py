from flask import Blueprint, request
from controllers.admission_data import AdmissionScoreController

admission_score_bp = Blueprint("admission_score", __name__, url_prefix="/api/admission-scores")

@admission_score_bp.route("/", methods=["GET"])
def get_all():
    return AdmissionScoreController.get_all()

@admission_score_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    return AdmissionScoreController.get_by_id(id)

@admission_score_bp.route("/", methods=["POST"])
def create():
    return AdmissionScoreController.create(request.json)

@admission_score_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return AdmissionScoreController.update(id, request.json)

@admission_score_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return AdmissionScoreController.delete(id)
