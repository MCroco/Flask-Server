from os import environ

class Config:
	# General
	TESTING = environ.get('TESTING')
	FLASK_DEBUG = environ.get('FLASK_DEBUG')
	SECRET_KEY = environ.get('SECRET_KEY')

	# Database
	SQLALCHEMY_DATABASE_URI = environ.get('URI') + environ.get('DATABASE_USER') + \
								':' + environ.get('DATABASE_PASSWORD') + \
								'@' + environ.get('APP_NAME') + '_database:' + \
								environ.get('DATABASE_PORT') + '/' + environ.get('DATABASE_NAME')
	SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('TRACK_MODIFICATION')
