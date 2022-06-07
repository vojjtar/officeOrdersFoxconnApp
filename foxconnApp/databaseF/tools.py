import sqlite3

def createConnection():
    conn = None
    try:
        conn = sqlite3.connect('foxconnApp/databaseF/equipment.db')
    except Exception as e:
        print(e)

    return conn

