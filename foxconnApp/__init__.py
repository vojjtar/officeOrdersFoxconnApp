from flask import Flask
from decouple import config

# creating flask app and specifying the html/css file locations
app = Flask(__name__,
            template_folder='www/templates',
            static_folder='www/static')
app.secret_key = config('SECRET_KEY')


# importing the views from foxconnApp package
from foxconnApp import views
from foxconnApp import order
from foxconnApp import api
