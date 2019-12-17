""" Code for App """

from flask import Flask
from .models import DB

def create_app():
    app = Flask(__name__)

    #add config to Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # have the database know
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!!'
    return app