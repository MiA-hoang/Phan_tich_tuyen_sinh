from flask import Blueprint, request
from controllers.university import UniversityController

university_bp = Blueprint("university", __name__, url_prefix="/api/universities")

@university_bp.route("/", methods=["GET"])
def get_all():
    return UniversityController.get_all()

@university_bp.route("/<string:id>", methods=["GET"])
def get_by_id(id):
    return UniversityController.get_by_id(id)

@university_bp.route("/", methods=["POST"])
def create():
    return UniversityController.create(request.json)

@university_bp.route("/<string:id>", methods=["PUT"])
def update(id):
    return UniversityController.update(id, request.json)

@university_bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return UniversityController.delete(id)
