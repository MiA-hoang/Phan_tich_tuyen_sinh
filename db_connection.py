import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-9C1G29S;'
    'Database=DuAn;'  
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()