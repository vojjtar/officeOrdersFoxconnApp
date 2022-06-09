import sqlite3
from foxconnApp import app

from flask import redirect, render_template, request, session, url_for

import time

from foxconnApp.databaseF import tools

@app.route('/order', methods=["POST"])
def order():
    if request.method == "POST": 

        data = request.form

        # getting the data from the form
        date = int(time.time())
        id = session["orderID"]

        email = data['email']
        name = data['name']
        surname = data['surname']

        pencil_quantity = int(data.get('quantity-pencil'))
        binder_quantity = int(data.get('quantity-binder'))
        pen_quantity = int(data.get('quantity-pen'))


        # checking if user didnt leave the form empty
        if pencil_quantity == binder_quantity == pen_quantity == 0:
            return redirect(url_for('.orderPage', orderMessage='You need to choose at least one product!'))
        if email == '' or name == '' or surname == '':
            return redirect(url_for('.orderPage', orderMessage='You cannot leave anything empty!'))
        else:
            try:
                conn = tools.createConnection()
                cur = conn.cursor()
                setting = cur.execute("SELECT name, price, quantityLimit FROM equipment")
            except sqlite3.Error as er:
                print(er)
                return 'there was an error connecting to our database try again later'


            totalPrice = 0
            finishData = []

            # calculating the price and creating a model to return
            for item in setting:
                itemName = item[0]
                itemPrice = float(item[1])
                itemLimit = int(item[2])
                item_quantity = 0

                # deciding the quantity of items this is probably really terrible way of doing it
                if itemName == 'pencil':
                    item_quantity = pencil_quantity
                if itemName == 'binder':
                    item_quantity = binder_quantity
                if itemName == 'pen':
                    item_quantity = pen_quantity

                # checking if the quantity is not 0 but also not over the specified limit in database
                # and appending to the list for later display
                if item_quantity >= 0 and item_quantity <= itemLimit:
                    totalPriceForItem = item_quantity * itemPrice
                    totalPrice += item_quantity * itemPrice
                    finishData.append({"name": itemName, "quantity": item_quantity, "price": itemPrice, "totalPriceForItem": totalPriceForItem})
                else:
                    return redirect(url_for('.orderPage', orderMessage='You cannot choose more than 10 items each!'))


            # rounding the total float to two decimal points
            totalPrice = round(totalPrice, 2)

            try:
                # inserting the order into the database
                query = "INSERT INTO orders (date, personalId, email, name, surname, pencil, binder, pen, price, processed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                params = (date, id, email, name, surname, pencil_quantity, binder_quantity, pen_quantity, totalPrice, 0)
                cur.execute(query, params)

                conn.commit()
            except sqlite3.Error as er:
                print(er)
                return 'there was an error with our database try again later'
            # putting the price in a session so that the user cannot change it
            session['totalPrice'] = totalPrice

            return render_template("order/finishOrder.html", finishData=finishData, totalPrice=session['totalPrice'])
    

@app.route('/finishOrder', methods=["POST"])
def finishOrder():
    # this could also be used as api endpoint for changing the processed status of an order by adding if GET etc...
    if request.method == 'POST':
        orderID = session['orderID']

        try:
            # setting order as processed after user decides to finish it
            conn = tools.createConnection()
            cur = conn.cursor()
            cur.execute(f"UPDATE orders SET processed = 1 WHERE personalId = '{orderID}'")
            conn.commit()
        except sqlite3.Error as er:
            print(er)
            return 'there was an error with our database try again later'

        # redirecting back to the order page with a successful message
        return redirect(url_for('.orderPage', orderMessage='Order finished! :)'))
    return 'error'
