from flask import jsonify
from services.major import MajorService
from schemas.major import MajorCreate, MajorUpdate, MajorResponse
from marshmallow import ValidationError

class MajorController:
    @staticmethod
    def get_all():
        return jsonify(MajorResponse(many=True).dump(MajorService.get_all())), 200

    @staticmethod
    def get_by_id(id):
        major = MajorService.get_by_id(id)
        if not major:
            return jsonify({"message": "Major not found"}), 404
        return jsonify(MajorResponse().dump(major)), 200

    @staticmethod
    def create(data):
        try:
            validated = MajorCreate().load(data)
            major = MajorService.create(validated)
            return jsonify(MajorResponse().dump(major)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def update(id, data):
        try:
            validated = MajorUpdate().load(data)
            major = MajorService.update(id, validated)
            if not major:
                return jsonify({"message": "Major not found"}), 404
            return jsonify(MajorResponse().dump(major)), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def delete(id):
        major = MajorService.delete(id)
        if not major:
            return jsonify({"message": "Major not found"}), 404
        return jsonify({"message": "Deleted successfully"}), 200
