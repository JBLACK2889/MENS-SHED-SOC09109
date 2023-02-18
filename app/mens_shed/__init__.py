#This is the file which tells python that this is a package and also initalises and ties together everything we need for the app

from flask import Flask


app = Flask(__name__)

#The Routes import must be kept after the app declaration otherwise you will get a circular import error
from mens_shed import route