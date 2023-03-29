#This is the file that contains all the logic for each page route

from flask import render_template, request, session, redirect, url_for, flash
from mens_shed import app, bcrypt
from mens_shed.forms import RegisterForm, LoginForm, ToolForm
from flask_login import login_required, login_manager, login_user, logout_user, current_user
from mens_shed.modules import User
import sqlite3
from mens_shed import app

#Set up database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    return conn


#This is the home page route
@app.route("/")
@app.route("/home")
def home():
        if current_user.is_authenticated:
            return redirect(url_for('about'))
        return render_template('home.html', title='Home')

#This is the about page route
@app.route("/about")
def about():
    return render_template('about.html', title='About')


#This is the booking page route
@app.route("/booking")
def booking():
    return render_template('booking.html', title='Booking')

#This is the Admin page route
@app.route("/admin")
def admin():
    return render_template('admin.html', title='Admin')

#This is the tools library page route
@app.route("/tools")
def tools():
    form = ToolForm()
    results = []


    if form.validate_on_submit():
        search = form.search.data 

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()

        cursor.execute("SELECT item, catagory, date_listed, picture FROM Tools WHERE item LIKE ?", ('%' + search + '%',))
        results = cursor.fetchall()
    return render_template('tools.html', title='Tools', form=form, results=results)

#This is the resource page route
@app.route("/resource", methods=['GET', 'POST'])
def resource():
    return render_template('resource.html', title='Resources')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = ToolForm()
    results = []

    if form.validate_on_submit():
        search = form.search.data

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()

        cursor.execute("SELECT item, catagory, date_listed, picture FROM Tools WHERE item LIKE ?", ('%' + search + '%',))
        results = cursor.fetchall()

    return render_template('search.html', form=form, results=results)


#This is the support page route
@app.route("/support")
def support():
    return render_template('support.html', title='Support')

#This is the signup page route
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()

        # Check if the username already exists in the database
        existing_user = c.execute('SELECT username FROM Users WHERE username = ?', (form.username.data,)).fetchone()

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            conn.close()
            return redirect(url_for('signup'))
        
        # Check if the username already exists in the database
        existing_email = c.execute('SELECT email FROM Users WHERE email = ?', (form.email.data,)).fetchone()

        if existing_email:
            flash('Email already exists. Please choose a different one.', 'danger')
            conn.close()
            return redirect(url_for('signup'))

        # If the username doesn't exist, insert the new user into the database
        else:
            c.execute('INSERT INTO Users (username, email, name, address, password) VALUES (?, ?, ?, ?, ?)',
                      (form.username.data, form.email.data, form.name.data, form.address.data, bcrypt.generate_password_hash(form.password.data).decode('utf-8')))
            conn.commit()
            conn.close()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('login_url'))
        
    return render_template('signup.html', title='Signup', form=form)

#This is the login page route
@app.route("/login", methods=['POST', 'GET'])
def login_url():
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()
        c.execute('SELECT * FROM Users WHERE email=? AND password=?',
                  (form.email.data, form.password.data))
        user = c.fetchone()
        conn.close()
        # Function to Kepp user details in the session
        if user:
            session['email'] = user[0]  # store user email in session
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))