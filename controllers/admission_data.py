from flask import jsonify, request
from services.admission_data import AdmissionScoreService
from schemas.admission_data import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
from marshmallow import ValidationError

def make_response(success, message, data=None, status=200):
    response = APIResponse().dump({"success": success, "message": message, "data": data})
    return jsonify(response), status

class AdmissionScoreController:
    @staticmethod
    def get_all():
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        pagination = AdmissionScoreService.get_all_paginated(page, limit)
        result = AdmissionScoreResponse(many=True).dump(pagination.items)
        return make_response(True, "List of admission scores", {
            "items": result,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": page
        })

    @staticmethod
    def get_by_id(Data_id):
        score = AdmissionScoreService.get_by_id(Data_id)
        return make_response(True, "Admission score details", AdmissionScoreResponse().dump(score)) if score else make_response(False, "Score not found", None, 404)

    @staticmethod
    def create(data):
        try:
            validated = AdmissionScoreCreate().load(data)
            score = AdmissionScoreService.create(validated)
            return make_response(True, "Admission score created successfully", AdmissionScoreResponse().dump(score), 201)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def update(Data_id, data):
        try:
            validated = AdmissionScoreUpdate().load(data)
            score = AdmissionScoreService.update(Data_id, validated)
            return make_response(True, "Admission score updated successfully", AdmissionScoreResponse().dump(score)) if score else make_response(False, "Score not found", None, 404)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def delete(Data_id):
        score = AdmissionScoreService.delete(Data_id)
        return make_response(True, "Deleted successfully", None) if score else make_response(False, "Score not found", None, 404)