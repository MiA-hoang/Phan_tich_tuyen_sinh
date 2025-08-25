from flask import Blueprint, request
from controllers.major import MajorController

major_bp = Blueprint("major", __name__, url_prefix="/api/majors")

@major_bp.route("/", methods=["GET"])
def get_all():
      """
      Get all majors
      ---
      responses:
        200:
          description: List of majors
          schema:
            type: array
            items:
              $ref: '#/components/schemas/MajorResponse'
      """
      return MajorController.get_all()

@major_bp.route("/<string:major_id>", methods=["GET"])
def get_by_id(major_id):
      """
      Get major by ID
      ---
      parameters:
        - name: major_id
          in: path
          type: string
          required: true
          description: The ID of the major
      responses:
        200:
          description: Major details
          schema:
            $ref: '#/components/schemas/MajorResponse'
        404:
          description: Major not found
      """
      return MajorController.get_by_id(major_id)

@major_bp.route("/", methods=["POST"])
def create():
      """
      Create a new major
      ---
      parameters:
        - name: body
          in: body
          required: true
          schema:
            $ref: '#/components/schemas/MajorCreate'
      responses:
        201:
          description: Created major
          schema:
            $ref: '#/components/schemas/MajorResponse'
        400:
          description: Validation error
      """
      return MajorController.create(request.json)

@major_bp.route("/<string:major_id>", methods=["PUT"])
def update(major_id):
      """
      Update major by ID
      ---
      parameters:
        - name: major_id
          in: path
          type: string
          required: true
          description: The ID of the major
        - name: body
          in: body
          required: true
          schema:
            $ref: '#/components/schemas/MajorUpdate'
      responses:
        200:
          description: Updated major
          schema:
            $ref: '#/components/schemas/MajorResponse'
        400:
          description: Validation error
        404:
          description: Major not found
      """
      return MajorController.update(major_id, request.json)

@major_bp.route("/<string:major_id>", methods=["DELETE"])
def delete(major_id):
      """
      Delete major by ID
      ---
      parameters:
        - name: major_id
          in: path
          type: string
          required: true
          description: The ID of the major
      responses:
        200:
          description: Deleted successfully
        404:
          description: Major not found
      """
      return MajorController.delete(major_id)