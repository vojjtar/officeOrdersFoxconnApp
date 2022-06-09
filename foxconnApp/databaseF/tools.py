import sqlite3
import string
import secrets

def createConnection():
    conn = None
    try:
        conn = sqlite3.connect('foxconnApp/databaseF/equipment.db')
    except Exception as e:
        print(e)

    return conn

def getPersonalId():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(7))
    
    return password

