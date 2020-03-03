from flask import render_template, Markup, request, make_response, Blueprint, url_for, redirect, flash, session
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from Application import db, login_manager
from Application.models.users import User
from Application.forms.LoginForm import LoginForm

logout_bp = Blueprint('logout_bp', __name__, template_folder='templates', static_folder='static')

@logout_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_bp.login'))