from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

# All blueprints have to be put under the 'db' initialization to avoid
# a circular import
from .home import home_routes
from .contact import contact_routes
from .signin import signin_routes
from .login import login_routes
from .logout import logout_routes
from .static import bootstrap_routes

def init_app():
    app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
    app.config.from_object('config.Config')

    app.register_blueprint(home_routes.home_bp)
    app.register_blueprint(contact_routes.contact_bp)
    app.register_blueprint(signin_routes.signin_bp)
    app.register_blueprint(login_routes.login_bp)
    app.register_blueprint(logout_routes.logout_bp)
    app.register_blueprint(bootstrap_routes.bootstrap_bp)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        db.create_all()

        return app