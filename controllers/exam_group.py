from flask import jsonify, request
from services.exam_group import ExamGroupService
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse
from marshmallow import ValidationError

def make_response(success, message, data=None, status=200):
    response = APIResponse().dump({"success": success, "message": message, "data": data})
    return jsonify(response), status

class ExamGroupController:
    @staticmethod
    def get_all():
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        pagination = ExamGroupService.get_all_paginated(page, limit)
        result = ExamGroupResponse(many=True).dump(pagination.items)
        return make_response(True, "List of exam groups", {
            "items": result,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": page
        })

    @staticmethod
    def get_by_id(group_code):  
        group = ExamGroupService.get_by_group_code(group_code)  
        return make_response(True, "Exam group details", ExamGroupResponse().dump(group)) if group else make_response(False, "Exam group not found", None, 404)

    @staticmethod
    def create(data):
        try:
            validated = ExamGroupCreate().load(data)
            group = ExamGroupService.create(validated)
            return make_response(True, "Exam group created successfully", ExamGroupResponse().dump(group), 201)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def update(group_code, data):  
        try:
            validated = ExamGroupUpdate().load(data)
            group = ExamGroupService.update(group_code, validated)
            return make_response(True, "Exam group updated successfully", ExamGroupResponse().dump(group)) if group else make_response(False, "Exam group not found", None, 404)
        except ValidationError as err:
            return make_response(False, err.messages, None, 400)

    @staticmethod
    def delete(group_code):  
        group = ExamGroupService.delete(group_code)
        return make_response(True, "Deleted successfully", None) if group else make_response(False, "Exam group not found", None, 404)