from flask import render_template, Markup, request, make_response, Blueprint
from flask import current_app as app
from datetime import datetime
from Application import db
from Application.models.FormModel import FormModel

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/', methods=['GET'])
def test_funct():
	name = request.args.get('name')
	if name:
		existing_name = FormModel.query.filter(FormModel.name == name).first()
		if existing_name:
			return make_response(f'{name} already exist')
		new_formmodel = FormModel(name=name)
		db.session.add(new_formmodel)
		db.session.commit()
	
	forms=FormModel.query.all()
	return render_template('example.html', forms=forms, title='Show FormModel')
