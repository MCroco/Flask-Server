from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

# Blueprints under
from Application.home import home_routes

def init_app():
	app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
	app.config.from_object('config.Config')

	app.register_blueprint(home_routes.home_bp)

	db.init_app(app)
	#login_manager.init_app(app)

	with app.app_context():
		db.create_all()

		return app
