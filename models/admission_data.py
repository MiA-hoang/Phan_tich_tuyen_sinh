from database import db

class AdmissionScore(db.Model):
    __tablename__ = "ADMISSION_SCORES"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    university_id = db.Column(db.String(10), db.ForeignKey("UNIVERSITIES.id"), nullable=False)
    major_id = db.Column(db.String(10), db.ForeignKey("MAJORS.major_id"), nullable=False)
    year = db.Column(db.Integer)
    min_score = db.Column(db.Float)
    quota = db.Column(db.Integer)
    note = db.Column(db.Text)
    group_code = db.Column(db.String(10), db.ForeignKey("EXAM_GROUPS.group_code"))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)