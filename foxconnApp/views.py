# importing flask app from the foxconnApp package
import sqlite3
from foxconnApp import app

# importing needed library for rendering html templates
from flask import render_template, session, request

from foxconnApp.databaseF import tools

from datetime import datetime


# main page for ordering equipment
@app.route('/orderPage')
def orderPage():
    try:
        conn = tools.createConnection()
        cur = conn.cursor()
        # getting equipment from the database
        cur.execute("SELECT name, price, quantityLimit FROM equipment")
        rows = cur.fetchall()
    except sqlite3.Error as er:
        print(er)
        return 'there was an error connecting to our database try again later'

    data = []

    # putting all the items in a list
    for row in rows:
        model = {
            "name": row[0],
            "price": row[1],
            "limit": row[2],
        }
        data.append(model)

    # setting the order ID as a session variable so users cant change them themselves
    session["orderID"] = tools.getPersonalId()

    try:
        # getting information about last 3 orders from the database and putting them in a list
        cur.execute("SELECT date, name, surname, price, personalId FROM orders WHERE processed = 1 ORDER BY date DESC LIMIT 3")

        rows = cur.fetchall()
    except sqlite3.Error as er:
        print(er)
        return 'there was an error connecting to our database try again later'

    dataOrders = []

    for row in rows:
        model = {
            # changing the date from unix timestamp to a readable date using datetime library
            "date": datetime.utcfromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S'),
            "name": row[1],
            "surname": row[2],
            "price": row[3],
            "personalId": row[4]
        }
        dataOrders.append(model)


    try:
        # getting info about the total price of unprocessed orders and checking if its None. If so it is set to 0
        cur.execute("SELECT SUM(price) FROM orders WHERE processed = 0")
    except sqlite3.Error as er:
        print(er)


    priceForNotProcessed = cur.fetchone()[0]
    if priceForNotProcessed == None:
        priceForNotProcessed = 0

    return render_template('order/orderPage.html', data=data, dataOrders=dataOrders, priceForNotProcessed=priceForNotProcessed, personalId=session["orderID"], orderMessage=request.args.get('orderMessage'))