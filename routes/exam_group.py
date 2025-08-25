from flask import Blueprint, request
from controllers.exam_group import ExamGroupController

exam_group_bp = Blueprint("exam_group", __name__, url_prefix="/api/exam-groups")

@exam_group_bp.route("/", methods=["GET"])
def get_all():
    """
    Get all exam groups
    ---
    responses:
      200:
        description: List of exam groups
        schema:
          type: array
          items:
            $ref: '#/components/schemas/ExamGroup'
    """
    return ExamGroupController.get_all()

@exam_group_bp.route("/<string:group_code>", methods=["GET"])
def get_by_id(group_code):
    """
    Get exam group by ID
    ---
    parameters:
      - name: group_code
        in: path
        type: string
        required: true
        description: The group code of the exam group
    responses:
      200:
        description: Exam group details
        schema:
          $ref: '#/components/schemas/ExamGroup'
      404:
        description: Exam group not found
    """
    return ExamGroupController.get_by_id(group_code)

@exam_group_bp.route("/", methods=["POST"])
def create():
    """
    Create a new exam group
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/components/schemas/ExamGroupCreate'
    responses:
      201:
        description: Created exam group
        schema:
          $ref: '#/components/schemas/ExamGroup'
      400:
        description: Validation error
    """
    return ExamGroupController.create(request.json)

@exam_group_bp.route("/<string:group_code>", methods=["PUT"])
def update(group_code):
    """
    Update exam group by ID
    ---
    parameters:
      - name: group_code
        in: path
        type: string
        required: true
        description: The group code of the exam group
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/components/schemas/ExamGroupUpdate'
    responses:
      200:
        description: Updated exam group
        schema:
          $ref: '#/components/schemas/ExamGroup'
      400:
        description: Validation error
      404:
        description: Exam group not found
    """
    return ExamGroupController.update(group_code, request.json)

@exam_group_bp.route("/<string:group_code>", methods=["DELETE"])
def delete(group_code):
    """
    Delete exam group by ID
    ---
    parameters:
      - name: group_code
        in: path
        type: string
        required: true
        description: The group code of the exam group
    responses:
      200:
        description: Deleted successfully
      404:
        description: Exam group not found
    """
    return ExamGroupController.delete(group_code)