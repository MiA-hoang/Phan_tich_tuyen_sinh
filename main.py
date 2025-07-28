import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from app import app_routes

from routes.university import university_bp
from routes.major import major_bp
from routes.exam_group import exam_group_bp
from routes.admission_data import admission_data_bp

app = Flask(__name__)

app.register_blueprint(app_routes)


# Đăng ký blueprint từ routes với tiền tố /api/ để tránh xung đột URL 
app.register_blueprint(university_bp, url_prefix='/api/universities')
app.register_blueprint(major_bp, url_prefix='/api/majors')
app.register_blueprint(exam_group_bp, url_prefix='/api/exam_groups')
app.register_blueprint(admission_data_bp, url_prefix='/api/admission_data')

# Trang chủ
@app.route("/")
def home():
    return "Welcome to Tuyển Sinh API!"
if __name__ == "__main__":
    app.run(debug=True)
