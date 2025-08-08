from flask import Blueprint, request
from controllers.major import MajorController

major_bp = Blueprint("major", __name__, url_prefix="/api/majors")

@major_bp.route("/", methods=["GET"])
def get_all():
    return MajorController.get_all()

@major_bp.route("/<string:id>", methods=["GET"])
def get_by_id(id):
    return MajorController.get_by_id(id)

@major_bp.route("/", methods=["POST"])
def create():
    return MajorController.create(request.json)

@major_bp.route("/<string:id>", methods=["PUT"])
def update(id):
    return MajorController.update(id, request.json)

@major_bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return MajorController.delete(id)
