from flask import Flask

# creating flask app and specifying the html/css file locations
app = Flask(__name__,
            template_folder='www/templates',
            static_folder='www/static')

# importing the views from foxconnApp package
from foxconnApp import views
from foxconnApp import order

