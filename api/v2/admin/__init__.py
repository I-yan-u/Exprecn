from flask import Blueprint
from config import FLASK

admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.secret_key = FLASK['admin']

from api.v2.admin.index import *