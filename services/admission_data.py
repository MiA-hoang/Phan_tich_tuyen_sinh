from models.admission_data import AdmissionScore
from database import db

class AdmissionScoreService:
    @staticmethod
    def get_all():
        return AdmissionScore.query.all()

    @staticmethod
    def get_all_paginated(page, limit):
        if not isinstance(page, int) or not isinstance(limit, int) or page < 1 or limit < 1:
            page = 1
            limit = 10
        return AdmissionScore.query.paginate(page=page, per_page=limit, error_out=False)

    @staticmethod
    def get_by_id(Data_id):
        return AdmissionScore.query.get(Data_id)

    @staticmethod
    def create(data):
        score = AdmissionScore(**data)
        db.session.add(score)
        db.session.commit()
        return score

    @staticmethod
    def update(Data_id, data):
        score = AdmissionScore.query.get(Data_id)
        if score:
            for key, value in data.items():
                setattr(score, key, value)
            db.session.commit()
        return score

    @staticmethod
    def delete(Data_id):
        score = AdmissionScore.query.get(Data_id)
        if score:
            db.session.delete(score)
            db.session.commit()
        return score