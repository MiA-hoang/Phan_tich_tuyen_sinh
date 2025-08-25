from flask import jsonify, request
from services.university import UniversityService
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
from marshmallow import ValidationError

def make_response(success, message, data=None, status=200):
    response = APIResponse().dump({"success": success, "message": message, "data": data})
    return jsonify(response), status

class UniversityController:
    @staticmethod
    def get_all():
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        pagination = UniversityService.get_all_paginated(page, limit)
        result = UniversityResponse(many=True).dump(pagination.items)
        return make_response(True, "List of universities", {
            "items": result,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": page
        })

    @staticmethod
    def get_by_id(id):
        university = UniversityService.get_by_id(id)
        return make_response(True, "University details", UniversityResponse().dump(university)) if university else make_response(False, "University not found", None, 404)

    @staticmethod
    def create(data):
        try:
            validated = UniversityCreate().load(data)
            university = UniversityService.create(validated)
            return make_response(True, "Post created successfully", UniversityResponse().dump(university), 201)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def update(id, data):
        try:
            validated = UniversityUpdate().load(data)
            university = UniversityService.update(id, validated)
            return make_response(True, "University updated successfully", UniversityResponse().dump(university)) if university else make_response(False, "University not found", None, 404)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def delete(id):
        university = UniversityService.delete(id)
        return make_response(True, "Deleted successfully", None) if university else make_response(False, "University not found", None, 404)