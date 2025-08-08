from models.university import University
from database import db

class UniversityService:
    @staticmethod
    def get_all():
        return University.query.all()

    @staticmethod
    def get_by_id(id):
        return University.query.get(id)

    @staticmethod
    def create(data):
        university = University(**data)
        db.session.add(university)
        db.session.commit()
        return university

    @staticmethod
    def update(id, data):
        university = University.query.get(id)
        if university:
            for key, value in data.items():
                setattr(university, key, value)
            db.session.commit()
        return university

    @staticmethod
    def delete(id):
        university = University.query.get(id)
        if university:
            db.session.delete(university)
            db.session.commit()
        return university
