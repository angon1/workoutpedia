from app import app, db
from app.users.models import *
from app.excercises.models import *

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Excercise': Excercise, 'Tag':Tag}
