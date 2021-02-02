from flask import Blueprint

bp = Blueprint("exercises", __name__, template_folder="templates")

from app.exercises import routes
