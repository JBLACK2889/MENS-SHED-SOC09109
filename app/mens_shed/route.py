#This is the file that contains all the logic for each page route

from flask import render_template
from mens_shed import app


#This is the home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')