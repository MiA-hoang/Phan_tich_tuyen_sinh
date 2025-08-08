from flask import jsonify
from services.admission_data import AdmissionScoreService
from schemas.admission_data import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse
from marshmallow import ValidationError

class AdmissionScoreController:
    @staticmethod
    def get_all():
        return jsonify(AdmissionScoreResponse(many=True).dump(AdmissionScoreService.get_all())), 200

    @staticmethod
    def get_by_id(id):
        score = AdmissionScoreService.get_by_id(id)
        if not score:
            return jsonify({"message": "Score not found"}), 404
        return jsonify(AdmissionScoreResponse().dump(score)), 200

    @staticmethod
    def create(data):
        try:
            validated = AdmissionScoreCreate().load(data)
            score = AdmissionScoreService.create(validated)
            return jsonify(AdmissionScoreResponse().dump(score)), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def update(id, data):
        try:
            validated = AdmissionScoreUpdate().load(data)
            score = AdmissionScoreService.update(id, validated)
            if not score:
                return jsonify({"message": "Score not found"}), 404
            return jsonify(AdmissionScoreResponse().dump(score)), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    @staticmethod
    def delete(id):
        score = AdmissionScoreService.delete(id)
        if not score:
            return jsonify({"message": "Score not found"}), 404
        return jsonify({"message": "Deleted successfully"}), 200
