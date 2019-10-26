"""Flask application factory"""

from flask import Flask
from flask_migrate import Migrate
from flask_login import login_required, current_user
#from flask.ext.login import LoginManager , login_required , UserMixin , login_user, current_user
from flask import Blueprint, render_template

#thid id actually oauth
from app.views import api
from app.models import db

main = Blueprint('main', __name__)

#todo index and profile are pages
@main.route('/')
def index():
    return render_template('Index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

#todo to move it to init
# def create_app():
#     """Create Flask application with given configuration"""
#     app = Flask(__name__, static_folder=None)
#     app.config.from_pyfile('config/hack.py')

#     db.init_app(app)
#     Migrate(app, db)

#     app.register_blueprint(api)

#     return app
