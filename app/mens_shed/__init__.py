#This is the file which tells python that this is a package and also initalises and ties together everything we need for the app
import sqlite3
from flask import Flask


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#The Routes import must be kept after the app declaration otherwise you will get a circular import error
from mens_shed import route