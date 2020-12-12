import os
from flask import Flask, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'users.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #inits
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    #blueprints
    from app.excercises import bp as excercises_bp
    app.register_blueprint(excercises_bp, url_prefix='/excercises')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #debugging
    if not app.debug and not app.testing:
        # hihi
        print("nothing")

    return app
