from flask import render_template, Markup, request, make_response, Blueprint, url_for, redirect, flash, session
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from Application import db, login_manager
from Application.models.users import User
from Application.forms.LoginForm import LoginForm

login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.create_image'))

    form=LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password=password):
                login_user(user)
                return redirect(url_for('home_bp.create_image'))
        flash('Invalid username/password')
        return redirect(url_for('contact_bp.contact'))
    
    return render_template('login.html', form=form, title='Log in.')

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('login_bp.login'))