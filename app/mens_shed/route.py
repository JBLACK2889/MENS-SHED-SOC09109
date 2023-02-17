from flask import render_template
from mens_shed import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')