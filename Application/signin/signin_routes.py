import os

from flask import render_template, Markup, request, make_response, Blueprint, url_for, redirect, flash, session
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from Application import db, login_manager
from Application.models.users import User
from Application.forms.SignInForm import SignInForm
from Application.home.home_routes import home_bp

signin_bp = Blueprint('signin_bp', __name__, template_folder='templates', static_folder='static')

@signin_bp.route('/signin', methods=['POST', 'GET'])
def signin():    
    form=SignInForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        website = request.form.get('website')
        created_on = datetime.now()
        existing_user = User.query.filter_by(name=name).first()
        existing_email = User.query.filter_by(email=email).first()
        if existing_user is None and existing_email is None:
            user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), website=website, created_on=created_on)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home_bp.create_image'))

    return render_template('signin.html', form=form, title='Create an Account')

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('login_bp.login'))