from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.secret_key = 'b0a747d7-c9aa-434c-2cc4360d0bc7'

from api.v2.admin.index import *