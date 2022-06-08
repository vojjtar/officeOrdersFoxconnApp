from json import tool
from os import abort
from foxconnApp import app

from flask import jsonify, redirect, render_template, request, session, url_for

import time

from foxconnApp.databaseF import tools

@app.route('/order', methods=["POST"])
def order():
    if request.method == "POST": 

        data = request.form
        print(data)

        date = int(time.time())
        id = session["orderID"]


        email = data['email']
        name = data['name']
        surname = data['surname']

        pencil_quantity = int(data.get('quantity-pencil'))
        binder_quantity = int(data.get('quantity-binder'))
        pen_quantity = int(data.get('quantity-pen'))



        if pencil_quantity == binder_quantity == pen_quantity == 0:
            return redirect(url_for('.orderPage', errorMessage='you need to choose at least one product!'))
        if email == name == surname != '':
            return redirect(url_for('.orderPage', errorMessage='you cannot leave anything empty!'))
        else:
            conn = tools.createConnection()
            cur = conn.cursor()

            setting = cur.execute("SELECT name, price, quantityLimit FROM equipment")

            totalPrice = 0

            finishData = []

            for item in setting:
                itemName = item[0]
                itemPrice = float(item[1])
                itemLimit = int(item[2])


                if itemName == 'pencil':
                    totalPrice += tools.checkItem(finishData, pencil_quantity, itemLimit, itemPrice, itemName, totalPrice)
                if itemName == 'binder':
                    totalPrice += tools.checkItem(finishData, binder_quantity, itemLimit, itemPrice, itemName, totalPrice)
                if itemName == 'pen':
                    totalPrice += tools.checkItem(finishData, pen_quantity, itemLimit, itemPrice, itemName, totalPrice)


            totalPrice = round(totalPrice, 2)

            query = "INSERT INTO orders (date, personalId, email, name, surname, pencil, binder, pen, price, processed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            params = (date, id, email, name, surname, pencil_quantity, binder_quantity, pen_quantity, totalPrice, 0)
            cur.execute(query, params)

            conn.commit()

            session['totalPrice'] = totalPrice

            return render_template("order/finishOrder.html", finishData=finishData, totalPrice=session['totalPrice'])
    

@app.route('/finishOrder', methods=["POST"])
def finishOrder():
    if request.method == 'POST':
        orderID = session['orderID']

        conn = tools.createConnection()

        cur = conn.cursor()
        cur.execute(f"UPDATE orders SET processed = 1 WHERE personalId = '{orderID}'")

        conn.commit()


        return redirect(url_for('.orderPage', errorMessage='orderFinished :)'))
    return abort(404)