# importing flask app from the foxconnApp package
from unicodedata import name
from foxconnApp import app

# importing needed library for rendering html templates
from flask import render_template

from foxconnApp.databaseF import tools

import sqlite3

# main page for ordering equipment
@app.route('/')
def index():
    conn = tools.createConnection()

    cur = conn.cursor()

    cur.execute("SELECT name, price, quantityLimit FROM equipment")

    rows = cur.fetchall()

    data = []

    for row in rows:
        print(row)

        model = {
            "name": row[0],
            "price": row[1],
            "limit": row[2],
        }
        data.append(model)

    print(data)



    return render_template('mainPage/index.html', data=data)