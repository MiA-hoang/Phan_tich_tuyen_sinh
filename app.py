from flask import Flask, jsonify
from db_connection import get_db_connection

app = Flask(__name__)

def fetch_all(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

@app.route("/universities")
def get_universities():
    return jsonify(fetch_all("SELECT * FROM UNIVERSITIES"))

@app.route("/majors")
def get_majors():
    return jsonify(fetch_all("SELECT * FROM MAJORS"))

@app.route("/exam_groups")
def get_exam_groups():
    return jsonify(fetch_all("SELECT * FROM EXAM_GROUPS"))

@app.route("/admission_scores")
def get_admission_scores():
    return jsonify(fetch_all("SELECT * FROM ADMISSION_SCORES"))
