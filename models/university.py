from database import db

class University(db.Model):
    __tablename__ = "UNIVERSITIES"

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50))
    city = db.Column(db.String(100))
    region = db.Column(db.String(50))