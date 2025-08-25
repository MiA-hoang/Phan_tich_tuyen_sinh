from flask import Blueprint, request
from controllers.university import UniversityController

university_bp = Blueprint("university", __name__, url_prefix="/api/universities")

@university_bp.route("/", methods=["GET"])
def get_all():
      """
      Get all universities
      ---
      responses:
        200:
          description: List of universities
          schema:
            type: array
            items:
              $ref: '#/components/schemas/UniversityResponse'
      """
      return UniversityController.get_all()

@university_bp.route("/<string:id>", methods=["GET"])
def get_by_id(id):
      """
      Get university by ID
      ---
      parameters:
        - name: id
          in: path
          type: string
          required: true
      responses:
        200:
          description: University details
          schema:
            $ref: '#/components/schemas/UniversityResponse'
        404:
          description: University not found
      """
      return UniversityController.get_by_id(id)

@university_bp.route("/", methods=["POST"])
def create():
      """
      Create a new university
      ---
      parameters:
        - name: body
          in: body
          required: true
          schema:
            $ref: '#/components/schemas/UniversityCreate'
      responses:
        201:
          description: Created university
          schema:
            $ref: '#/components/schemas/UniversityResponse'
        400:
          description: Validation error
      """
      return UniversityController.create(request.json)

@university_bp.route("/<string:id>", methods=["PUT"])
def update(id):
      """
      Update university by ID
      ---
      parameters:
        - name: id
          in: path
          type: string
          required: true
        - name: body
          in: body
          required: true
          schema:
            $ref: '#/components/schemas/UniversityUpdate'
      responses:
        200:
          description: Updated university
          schema:
            $ref: '#/components/schemas/UniversityResponse'
        400:
          description: Validation error
        404:
          description: University not found
      """
      return UniversityController.update(id, request.json)

@university_bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
      """
      Delete university by ID
      ---
      parameters:
        - name: id
          in: path
          type: string
          required: true
      responses:
        200:
          description: Deleted successfully
        404:
          description: University not found
      """
      return UniversityController.delete(id)