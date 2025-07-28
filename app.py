from flask import Blueprint, Response, request
import json
from db_connection import cursor

app_routes = Blueprint('app_routes', __name__, url_prefix='/classic')

@app_routes.route("/universities")
def get_universities():
    query = "SELECT * FROM UNIVERSITIES WHERE 1=1"
    params = []
    if request.args.get("name"):
        query += " AND name LIKE ?"
        params.append("%" + request.args.get("name") + "%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

@app_routes.route("/universities/<string:university_id>", methods=["DELETE"])
def delete_university(university_id):
    cursor.execute("DELETE FROM UNIVERSITIES WHERE university_id = ?", (university_id,))
    cursor.commit()
    return Response(json.dumps({"message": "University deleted successfully"}), 
                   content_type="application/json; charset=utf-8")

@app_routes.route("/majors")
def get_majors():
    query = "SELECT * FROM MAJORS WHERE 1=1"
    params = []
    if request.args.get("name"):
        query += " AND name LIKE ?"
        params.append("%" + request.args.get("name") + "%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

@app_routes.route("/majors/<string:major_id>", methods=["DELETE"])
def delete_major(major_id):
    cursor.execute("DELETE FROM MAJORS WHERE major_id = ?", (major_id,))
    cursor.commit()
    return Response(json.dumps({"message": "Major deleted successfully"}), 
                   content_type="application/json; charset=utf-8")

@app_routes.route("/exam_groups")
def get_exam_groups():
    query = "SELECT * FROM EXAM_GROUPS WHERE 1=1"
    params = []
    if request.args.get("description"):
        query += " AND description LIKE ?"
        params.append("%" + request.args.get("description") + "%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

@app_routes.route("/exam_groups/<string:group_code>", methods=["DELETE"])
def delete_exam_group(group_code):
    cursor.execute("DELETE FROM EXAM_GROUPS WHERE group_code = ?", (group_code,))
    cursor.commit()
    return Response(json.dumps({"message": "Exam group deleted successfully"}), 
                   content_type="application/json; charset=utf-8")

from datetime import datetime

@app_routes.route("/admission_scores")
def get_admission_scores():
    query = "SELECT * FROM ADMISSION_SCORES WHERE 1=1"
    params = []
    if request.args.get("year"):
        query += " AND year = ?"
        params.append(int(request.args.get("year")))
    if request.args.get("university_id"):
        query += " AND university_id = ?"
        params.append(request.args.get("university_id"))
    cursor.execute(query, params)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [],
    for row in rows:
        row_dict = dict(zip(columns, row))

        for key, value in row_dict.items():
            if isinstance(value, datetime):
                row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        data.append(row_dict)

    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

@app_routes.route("/admission_scores/<int:data_id>", methods=["DELETE"])
def delete_admission_score(data_id):
    cursor.execute("DELETE FROM ADMISSION_SCORES WHERE data_id = ?", (data_id,))
    cursor.commit()
    return Response(json.dumps({"message": "Admission score deleted successfully"}), 
                   content_type="application/json; charset=utf-8")

@app_routes.route("/")
def home():
    return "Welcome to Tuyển Sinh API !"
