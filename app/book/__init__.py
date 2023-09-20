from flask import Blueprint

book = Blueprint('book', __name__, url_prefix='/book')

from . import views