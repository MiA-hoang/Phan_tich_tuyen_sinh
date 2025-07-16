import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)


conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-9C1G29S;'   
    'Database=DuAn BIT;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

@app.route("/")
def home():
    return "Hello Tuyen Sinh!"


@app.route("/universities")
def get_universities():
    cursor.execute("SELECT * FROM UNIVERSITIES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])


@app.route("/majors")
def get_majors():
    cursor.execute("SELECT * FROM MAJORS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])


@app.route("/exam-groups")
def get_exam_groups():
    cursor.execute("SELECT * FROM EXAM_GROUPS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route("/admission-scores")
def get_admission_scores():
    cursor.execute("SELECT * FROM ADMISSION_SCORES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return jsonify([dict(zip(columns, row)) for row in rows])

if __name__ == "__main__":
    app.run(debug=True)