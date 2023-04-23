#This is the file which tells python that this is a package and also initalises and ties together everything we need for the app
import sqlite3
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = '460e9ab5e552fd6c30ede37d96298a41'
app.config['DATABASE'] = 'database.db'

# Initialize the LoginManager object
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


#The Routes import must be kept after the app declaration otherwise you will get a circular import error
from mens_shed import route