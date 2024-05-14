from flask import Blueprint
import config

admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.secret_key = config.FLASK['admin']

from api.v2.admin.index import *