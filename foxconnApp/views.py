# importing flask app from the foxconnApp package
from foxconnApp import app

# importing needed library for rendering html templates
from flask import render_template


# main page for ordering equipment
@app.route('/')
def index():
    return render_template('mainPage/index.html')