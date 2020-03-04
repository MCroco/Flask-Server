from wtforms import StringField, TextField, SubmitField, Form, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo, Optional

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter a valid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')