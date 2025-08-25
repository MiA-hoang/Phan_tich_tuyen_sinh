from models.exam_group import ExamGroup
from database import db

class ExamGroupService:
    @staticmethod
    def get_all():
        return ExamGroup.query.all()

    @staticmethod
    def get_all_paginated(page, limit):
        return ExamGroup.query.paginate(page=page, per_page=limit, error_out=False)

    @staticmethod
    def get_by_code(group_code):
        return ExamGroup.query.get(group_code)

    @staticmethod
    def create(data):
        exam_group = ExamGroup(**data)
        db.session.add(exam_group)
        db.session.commit()
        return exam_group

    @staticmethod
    def update(group_code, data):
        exam_group = ExamGroup.query.get(group_code)
        if exam_group:
            for key, value in data.items():
                setattr(exam_group, key, value)
            db.session.commit()
        return exam_group

    @staticmethod
    def delete(group_code):
        exam_group = ExamGroup.query.get(group_code)
        if exam_group:
            db.session.delete(exam_group)
            db.session.commit()
        return exam_group