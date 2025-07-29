import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask

from app import app_routes


from database import db
from routes.university import university_bp
from routes.major import major_bp
from routes.exam_group import exam_group_bp
from routes.admission_data import admission_data_bp


app = Flask(__name__)

app.register_blueprint(app_routes)
app.register_blueprint(university_bp, url_prefix='/api')
app.register_blueprint(major_bp, url_prefix='/api')
app.register_blueprint(exam_group_bp, url_prefix='/api')
app.register_blueprint(admission_data_bp, url_prefix='/api')

@app.route("/")
def home():
    return "Welcome to Tuyển Sinh API!"

if __name__ == "__main__":
    app.run(debug=True)

def create_app():
    app = Flask(__name__)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://localhost/DuAn?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(university_bp, url_prefix="/api/universities")
    app.register_blueprint(major_bp, url_prefix="/api/majors")
    app.register_blueprint(exam_group_bp, url_prefix="/api/exam-groups")
    app.register_blueprint(admission_data_bp, url_prefix="/api/admission-scores")


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

