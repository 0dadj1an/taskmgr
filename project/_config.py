import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'flasktaskr.db'
USERNAME = 'ivos'
PASSWORD = 'cisco123'
#WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = '91b407a4e95ac4c327691b0d489fb3ca7913c36b94fbdb8429bbd65edbfcaf09'
# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

