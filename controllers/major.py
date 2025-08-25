from flask import jsonify, request
from services.major import MajorService
from schemas.major import MajorCreate, MajorUpdate, MajorResponse, APIResponse
from marshmallow import ValidationError

def make_response(success, message, data=None, status=200):
    response = APIResponse().dump({"success": success, "message": message, "data": data})
    return jsonify(response), status

class MajorController:
    @staticmethod
    def get_all():
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        pagination = MajorService.get_all_paginated(page, limit)
        result = MajorResponse(many=True).dump(pagination.items)
        return make_response(True, "List of majors", {
            "items": result,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": page
        })

    @staticmethod
    def get_by_id(major_id):
        major = MajorService.get_by_id(major_id)
        return make_response(True, "Major details", MajorResponse().dump(major)) if major else make_response(False, "Major not found", None, 404)

    @staticmethod
    def create(data):
        try:
            validated = MajorCreate().load(data)
            major = MajorService.create(validated)
            return make_response(True, "Major created successfully", MajorResponse().dump(major), 201)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def update(major_id, data):
        try:
            validated = MajorUpdate().load(data)
            major = MajorService.update(major_id, validated)
            return make_response(True, "Major updated successfully", MajorResponse().dump(major)) if major else make_response(False, "Major not found", None, 404)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def delete(major_id):
        major = MajorService.delete(major_id)
        return make_response(True, "Deleted successfully", None) if major else make_response(False, "Major not found", None, 404)