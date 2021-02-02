from app import create_app, db
from app.users.models import *
from app.exercises.models import *

# from config import Config
# class ShellConfig(Config):
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'shell.db')


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Exercise": Exercise, "Tag": Tag}
