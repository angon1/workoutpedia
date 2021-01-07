from flask import Blueprint

bp = Blueprint("excercises", __name__, template_folder="templates")

from app.excercises import routes
