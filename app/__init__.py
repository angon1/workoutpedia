from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #inits
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    if not app.debug and not app.testing:
        # hihi
        print("nothing")

    return app
