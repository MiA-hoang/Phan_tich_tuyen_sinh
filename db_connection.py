import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=DESKTOP-9C1G29S;'     
        'Database=DuAn BIT;'            
        'Trusted_Connection=yes;'
    )
    return conn