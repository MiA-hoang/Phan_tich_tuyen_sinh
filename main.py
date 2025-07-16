from flask import Flask
from app import app_routes  # import Blueprint từ file app.py

app = Flask(__name__)
app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)