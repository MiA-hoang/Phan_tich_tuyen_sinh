from models.major import Major
from database import db

class MajorService:
    @staticmethod
    def get_all():
        return Major.query.all()

    @staticmethod
    def get_by_id(major_id):
        return Major.query.get(major_id)

    @staticmethod
    def create(data):
        major = Major(**data)
        db.session.add(major)
        db.session.commit()
        return major

    @staticmethod
    def update(major_id, data):
        major = Major.query.get(major_id)
        if major:
            for key, value in data.items():
                setattr(major, key, value)
            db.session.commit()
        return major

    @staticmethod
    def delete(major_id):
        major = Major.query.get(major_id)
        if major:
            db.session.delete(major)
            db.session.commit()
        return major
