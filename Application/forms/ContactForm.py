#from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, Form
from wtforms.validators import DataRequired, Length, Email

class ContactForm(Form):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not valid email address.')), DataRequired()])
    body = TextField('Message', [DataRequired(), Length(min=4, message=('Your message is too short.'))])

    #ImportError: cannot import name 'url_encode' from 'werkzeug' (/usr/local/lib/python3.8/site-packages/werkzeug/__init__.py)
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')