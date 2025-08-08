from flask import jsonify
from services.university import UniversityService
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse
from marshmallow import ValidationError

class UniversityController:
    @staticmethod
    def get_all():
        return jsonify(UniversityResponse(many=True).dump(UniversityService.get_all())), 200

    @staticmethod
    def get_by_id(id):
        university = UniversityService.get_by_id(id)
        if not university:
            return jsonify({"message": "University not found"}), 404
        return jsonify(UniversityResponse().dump(university)), 200

    @staticmethod
    def create(data):
        try:
            validated = UniversityCreate().load(data)
            university = UniversityService.create(validated)
            return jsonify(UniversityResponse().dump(university)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def update(id, data):
        try:
            validated = UniversityUpdate().load(data)
            university = UniversityService.update(id, validated)
            if not university:
                return jsonify({"message": "University not found"}), 404
            return jsonify(UniversityResponse().dump(university)), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def delete(id):
        university = UniversityService.delete(id)
        if not university:
            return jsonify({"message": "University not found"}), 404
        return jsonify({"message": "Deleted successfully"}), 200
