import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from app import app_routes
from routes.exam_group import exam_group_bp

app = Flask(__name__)
app.register_blueprint(app_routes)
app.register_blueprint(exam_group_bp)

if __name__ == "__main__":
    app.run(debug=True)