from foxconnApp import app
from foxconnApp.databaseF import tools

from flask import jsonify, request



@app.route('/getOrderInfo', methods=["GET"])
def getOrderInfo():
    if request.method == "GET":
        orderID = request.args.get('orderID')

        if orderID != None:
            conn = tools.createConnection()
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM orders WHERE personalId = '{orderID}'")
            data = cur.fetchone()

            jsonData = {}

            for i in range(0, len(data)):
                jsonData[cur.description[i][0]] = data[i]

            return jsonify(jsonData)

        return "please inser orderID parameter with a correct value"