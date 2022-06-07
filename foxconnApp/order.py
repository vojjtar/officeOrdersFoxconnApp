from crypt import methods
from foxconnApp import app

from flask import request

@app.route('/order', methods=["POST"])
def order():
    data = request.form
    print(data)

    id = request.form['idDiv']
    email = request.form['email']
    name = request.form['name']
    surname = request.form['surname']


    pencil = request.form['pencil'] 
    binder = request.form['binder']
    pen = request.form['pen']


    

    return 'equipment was ordered'