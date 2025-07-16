from flask import Blueprint, Response
import json
from db_connection import cursor

app_routes = Blueprint('app_routes', __name__)

@app_routes.route("/universities")
def get_universities():
    cursor.execute("SELECT * FROM UNIVERSITIES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")


@app_routes.route("/majors")
def get_majors():
    cursor.execute("SELECT * FROM MAJORS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")


@app_routes.route("/exam_groups")
def get_exam_groups():
    cursor.execute("SELECT * FROM EXAM_GROUPS")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")


from datetime import datetime

@app_routes.route("/admission_scores")
def get_admission_scores():
    cursor.execute("SELECT * FROM ADMISSION_SCORES")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    data = []
    for row in rows:
        row_dict = dict(zip(columns, row))
        # Convert datetime to string
        for key, value in row_dict.items():
            if isinstance(value, datetime):
                row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        data.append(row_dict)

    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

@app_routes.route("/")
def home():
    return "Welcome to Tuyển Sinh API!"