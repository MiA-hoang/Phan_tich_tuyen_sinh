import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=NGOC HA;'
    'Database=DuAn;'  
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()