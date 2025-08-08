from flask import Blueprint, request
from controllers.exam_group import ExamGroupController

exam_group_bp = Blueprint("exam_group", __name__, url_prefix="/api/exam-groups")

@exam_group_bp.route("/", methods=["GET"])
def get_all():
    return ExamGroupController.get_all()

@exam_group_bp.route("/<string:id>", methods=["GET"])
def get_by_id(id):
    return ExamGroupController.get_by_id(id)

@exam_group_bp.route("/", methods=["POST"])
def create():
    return ExamGroupController.create(request.json)

@exam_group_bp.route("/<string:id>", methods=["PUT"])
def update(id):
    return ExamGroupController.update(id, request.json)

@exam_group_bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return ExamGroupController.delete(id)
