from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Length(min=6), 
                        Email(message='Enter a valid email.',
                        DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                            Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Confirm Your Password', validators=[DataRequired(), 
                            EqualTo('password', message='Passwords must match')])

    website = StringField('Website', validators=[Optional()])
    submit = SubmitField('Register')