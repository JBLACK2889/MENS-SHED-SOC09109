#This is the file that contains all the logic for each page route

from flask import render_template
from mens_shed import app
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

#This is the home page route
@app.route("/")
@app.route("/home")
def home():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM Users').fetchall()
    conn.close()
    return render_template('home.html', users=users)