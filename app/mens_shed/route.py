#This is the file that contains all the logic for each page route

from flask import render_template
from mens_shed import app, bcrypt
import sqlite3

#Set up database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


#This is the home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


#This is the about page route
@app.route("/about")
def about():
    return render_template('about.html', title='About')


#This is the booking page route
@app.route("/booking")
def booking():
    return render_template('booking.html', title='Booking')


#This is the resource page route
@app.route("/resource")
def resource():
    return render_template('resource.html', title='Resources')


#This is the support page route
@app.route("/support")
def support():
    return render_template('support.html', title='Support')


#This is the login page route
@app.route("/login")
def login():
    return render_template('login.html', title='Login')