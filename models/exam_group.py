from database import db

class ExamGroup(db.Model):
    __tablename__ = "EXAM_GROUPS"

    group_code = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.Text)