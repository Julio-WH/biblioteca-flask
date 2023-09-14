from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .auth import auth

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    db.init_app(app)
    Migrate(app, db, directory='./migrations')
    return app