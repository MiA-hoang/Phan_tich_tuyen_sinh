from flask import Blueprint, request
from controllers.admission_data import AdmissionScoreController

admission_score_bp = Blueprint("admission_scores", __name__, url_prefix="/api/admission-scores")

@admission_score_bp.route("/", methods=["GET"])
def get_all():
    """
    Get all admission scores
    ---
    responses:
      200:
        description: List of admission scores
        schema:
          type: array
          items:
            $ref: '#/components/schemas/AdmissionScoreResponse'
    """
    return AdmissionScoreController.get_all()


@admission_score_bp.route("/<int:Data_id>", methods=["GET"])
def get_by_id(Data_id):
    """
    Get admission score by ID
    ---
    parameters:
      - name: Data_id
        in: path
        type: integer
        required: true
        description: The ID of the admission score
    responses:
      200:
        description: Admission score details
        schema:
          $ref: '#/components/schemas/AdmissionScoreResponse'
      404:
        description: Admission score not found
    """
    return AdmissionScoreController.get_by_id(Data_id)


@admission_score_bp.route("/", methods=["POST"])
def create():
    """
    Create a new admission score
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/components/schemas/AdmissionScoreCreate'
    responses:
      201:
        description: Created admission score
        schema:
          $ref: '#/components/schemas/AdmissionScoreResponse'
      400:
        description: Validation error
    """
    return AdmissionScoreController.create(request.json)


@admission_score_bp.route("/<int:Data_id>", methods=["PUT"])
def update(Data_id):
    """
    Update admission score by ID
    ---
    parameters:
      - name: Data_id
        in: path
        type: integer
        required: true
        description: The ID of the admission score
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/components/schemas/AdmissionScoreUpdate'
    responses:
      200:
        description: Updated admission score
        schema:
          $ref: '#/components/schemas/AdmissionScoreResponse'
      400:
        description: Validation error
      404:
        description: Admission score not found
    """
    return AdmissionScoreController.update(Data_id, request.json)


@admission_score_bp.route("/<int:Data_id>", methods=["DELETE"])
def delete(Data_id):
    """
    Delete admission score by ID
    ---
    parameters:
      - name: Data_id
        in: path
        type: integer
        required: true
        description: The ID of the admission score
    responses:
      200:
        description: Deleted successfully
      404:
        description: Admission score not found
    """
    return AdmissionScoreController.delete(Data_id)
