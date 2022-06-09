import sqlite3
from foxconnApp import app
from foxconnApp.databaseF import tools

from flask import jsonify, request


@app.route('/getOrderInfo/<orderID>', methods=["GET"])
def getOrderInfo(orderID):
    if request.method == "GET":
        #orderID = #request.args.get('orderID')
        if orderID != None:
            try:
                # getting all info about an order based on given ID
                conn = tools.createConnection()
                cur = conn.cursor()
                cur.execute(f"SELECT * FROM orders WHERE personalId = '{orderID}'")
                data = cur.fetchone()

                jsonData = {}

                # making a dictionary out of all the data
                for i in range(0, len(data)):
                    jsonData[cur.description[i][0]] = data[i]

                return jsonify(jsonData)
            except sqlite3.Error as er:
                print(er)
                return('there was error while finding specified order.')

        return "please insert orderID parameter with a correct value"

@app.route('/setOrderAsProcessed/<orderID>', methods=["GET"])
def setOrderAsProcessed(orderID):
    if request.method == "GET":
        if orderID != None:
            #orderID = request.args.get('orderID')

            # creating connection and setting a selected order as processed
            try:
                conn = tools.createConnection()
                cur = conn.cursor()
                cur.execute(f"UPDATE orders SET processed = 1 WHERE personalId = '{orderID}'")
                conn.commit()
            except sqlite3.Error as er:
                print(er)
                return('there was error while finding specified order.')

            return jsonify(f"order with the ID: '{orderID}' has been set as processed.")

    return "please insert orderID parameter with a correct value"

