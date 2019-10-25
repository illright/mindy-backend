"""Flask application factory"""

from flask import Flask
from flask_migrate import Migrate

from app.views import api
from app.models import db


def create_app():
    """Create Flask application with given configuration"""
    app = Flask(__name__, static_folder=None)
    app.config.from_pyfile('config/hack.py')

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(api)

    return app
