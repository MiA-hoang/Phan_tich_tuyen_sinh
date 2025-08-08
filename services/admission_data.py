from models.admission_data import AdmissionScore
from database import db

class AdmissionScoreService:
    @staticmethod
    def get_all():
        return AdmissionScore.query.all()

    @staticmethod
    def get_by_id(id):
        return AdmissionScore.query.get(id)

    @staticmethod
    def create(data):
        score = AdmissionScore(**data)
        db.session.add(score)
        db.session.commit()
        return score

    @staticmethod
    def update(id, data):
        score = AdmissionScore.query.get(id)
        if score:
            for key, value in data.items():
                setattr(score, key, value)
            db.session.commit()
        return score

    @staticmethod
    def delete(id):
        score = AdmissionScore.query.get(id)
        if score:
            db.session.delete(score)
            db.session.commit()
        return score
