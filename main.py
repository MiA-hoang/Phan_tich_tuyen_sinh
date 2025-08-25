from flask import Flask
from flasgger import Swagger
from database import db
from routes.university import university_bp
from routes.major import major_bp
from routes.exam_group import exam_group_bp
from routes.admission_data import admission_score_bp
from marshmallow import fields
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from schemas.university import UniversityCreate, UniversityResponse, UniversityUpdate
from schemas.major import MajorCreate, MajorResponse, MajorUpdate
from schemas.exam_group import ExamGroupCreate, ExamGroupResponse, ExamGroupUpdate
from schemas.admission_data import AdmissionScoreCreate, AdmissionScoreResponse, AdmissionScoreUpdate

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://localhost/DuAn?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SWAGGER"] = {
        "title": "Tuyển Sinh API",
        "openapi": "3.0.2"  
    }
    db.init_app(app)

    spec = APISpec(
        title="Tuyển Sinh API",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[MarshmallowPlugin()],
    )

    spec.components.schema("UniversityCreate", schema=UniversityCreate)
    spec.components.schema("UniversityResponse", schema=UniversityResponse)
    spec.components.schema("UniversityUpdate", schema=UniversityUpdate)
    spec.components.schema("MajorCreate", schema=MajorCreate)
    spec.components.schema("MajorResponse", schema=MajorResponse)
    spec.components.schema("MajorUpdate", schema=MajorUpdate)
    spec.components.schema("ExamGroupCreate", schema=ExamGroupCreate)
    spec.components.schema("ExamGroupResponse", schema=ExamGroupResponse)
    spec.components.schema("ExamGroupUpdate", schema=ExamGroupUpdate)
    spec.components.schema("AdmissionScoreCreate", schema=AdmissionScoreCreate)
    spec.components.schema("AdmissionScoreResponse", schema=AdmissionScoreResponse)
    spec.components.schema("AdmissionScoreUpdate", schema=AdmissionScoreUpdate)

    Swagger(app, template=spec.to_dict())

    app.register_blueprint(university_bp, url_prefix="/api/universities")
    app.register_blueprint(major_bp, url_prefix="/api/majors")
    app.register_blueprint(exam_group_bp, url_prefix="/api/exam-groups")
    app.register_blueprint(admission_score_bp, url_prefix="/api/admission-scores")

    @app.route("/")
    def home():
        return "Welcome to Tuyển Sinh API!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)