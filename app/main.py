"""Flask application factory"""

from flask import Flask

from flask_login import login_required, current_user, LoginManager, UserMixin, login_user
from flask import Blueprint, render_template
from flask_migrate import Migrate

# thid id actually oauth
from .views import api
from .models import db

main = Blueprint('main', __name__)

# todo index and profile are pages
@main.route('/')
def index():
    return render_template('Index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# todo to move it to init


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/hack.py')
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost/mindy'

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(api)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .models import Account
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Account.query.get(int(user_id))

    return app
