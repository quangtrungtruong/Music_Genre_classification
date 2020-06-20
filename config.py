from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
	"""Set Flask configuration from .env file."""

	# General Config
	SECRET_KEY = environ.get('SECRET_KEY')
	FLASK_APP = environ.get('FLASK_APP')
	FLASK_ENV = environ.get('FLASK_ENV')

	# Database
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/Music_Genre_classification?charset=utf8'
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False