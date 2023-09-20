from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .auth import auth
from .author import author
from .book import book
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(author)
    app.register_blueprint(book)
    db.init_app(app)
    Migrate(app, db, directory='./migrations')
    return app
