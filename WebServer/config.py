import os
# define a base directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cits5206-2769'

    # Config database
    # Provide configuration variable or fallback value
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Disable tracking modifications, do not signal the application
    # every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False