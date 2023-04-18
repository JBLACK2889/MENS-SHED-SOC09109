from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, EmailField, SearchField, DateField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from flask_login import current_user
from mens_shed.modules import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Full Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
            

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ToolForm(FlaskForm):
    search = StringField('Search for a Tool')
    submit = SubmitField('Submit')

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    item_id = IntegerField('Item ID')
    booking_date = DateField('Booking Date', validators=[DataRequired()])
    start_time = TimeField('Start time', validators=[DataRequired()])
    end_time = TimeField('End time', validators=[DataRequired()])
    submit = SubmitField('Submit')