from flask import render_template, Markup, request, make_response, Blueprint, url_for, redirect
from flask import current_app as app
from datetime import datetime
from Application import db
from Application.forms.ContactForm import ContactForm

contact_bp = Blueprint('contact_bp', __name__, template_folder='templates', static_folder='static')

@contact_bp.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate():
        return redirect(url_for('success'))
    return render_template('contact_form.html', form=form)