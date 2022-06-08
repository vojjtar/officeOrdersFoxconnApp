# importing flask app from the foxconnApp package
from unicodedata import name
from foxconnApp import app

# importing needed library for rendering html templates
from flask import render_template, session, request

from foxconnApp.databaseF import tools

from datetime import datetime


# main page for ordering equipment
@app.route('/orderPage')
def orderPage():
    conn = tools.createConnection()
    cur = conn.cursor()

    cur.execute("SELECT name, price, quantityLimit FROM equipment")
    rows = cur.fetchall()

    data = []

    for row in rows:
        model = {
            "name": row[0],
            "price": row[1],
            "limit": row[2],
        }
        data.append(model)

    session["orderID"] = tools.getPersonalId()



    cur.execute("SELECT date, name, surname, price, personalId FROM orders WHERE processed = 1 ORDER BY date DESC LIMIT 3")

    rows = cur.fetchall()
    dataOrders = []

    for row in rows:
        model = {
            "date": datetime.utcfromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S'),
            "name": row[1],
            "surname": row[2],
            "price": row[3],
            "personalId": row[4]
        }
        dataOrders.append(model)



    cur.execute("SELECT SUM(price) FROM orders WHERE processed = 0")
    priceForNotProcessed = cur.fetchone()[0]
    if priceForNotProcessed == None:
        priceForNotProcessed = 0

    return render_template('order/orderPage.html', data=data, dataOrders=dataOrders, priceForNotProcessed=priceForNotProcessed, personalId=session["orderID"], errorMessage=request.args.get('errorMessage'))