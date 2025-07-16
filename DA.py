from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)


conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-9C1G29S;'
    'Database=DuAnBIT;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

@app.route("/")
def home():
    return 

@app.route("/universities")
def get_universities():
    cursor.execute("SELECT * FROM UNIVERSITIES")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)