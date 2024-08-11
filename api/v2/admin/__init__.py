from flask import Blueprint
from config import FLASK_CONFIG

flask = FLASK_CONFIG()

admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.secret_key = flask.admin

from api.v2.admin.admin import *