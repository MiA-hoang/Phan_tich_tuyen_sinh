from flask import jsonify
from services.exam_group import ExamGroupService
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse
from marshmallow import ValidationError

class ExamGroupController:
    @staticmethod
    def get_all():
        return jsonify(ExamGroupResponse(many=True).dump(ExamGroupService.get_all())), 200

    @staticmethod
    def get_by_id(id):
        group = ExamGroupService.get_by_id(id)
        if not group:
            return jsonify({"message": "Exam group not found"}), 404
        return jsonify(ExamGroupResponse().dump(group)), 200

    @staticmethod
    def create(data):
        try:
            validated = ExamGroupCreate().load(data)
            group = ExamGroupService.create(validated)
            return jsonify(ExamGroupResponse().dump(group)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def update(id, data):
        try:
            validated = ExamGroupUpdate().load(data)
            group = ExamGroupService.update(id, validated)
            if not group:
                return jsonify({"message": "Exam group not found"}), 404
            return jsonify(ExamGroupResponse().dump(group)), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def delete(id):
        group = ExamGroupService.delete(id)
        if not group:
            return jsonify({"message": "Exam group not found"}), 404
        return jsonify({"message": "Deleted successfully"}), 200

