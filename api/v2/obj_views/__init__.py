#!/usr/bin/python3
from flask import Blueprint
from config import FLASK

app_view = Blueprint('app_view', __name__, url_prefix='/exprecn')
app_view.secret_key = FLASK['app_view']

from api.v2.obj_views.index import *
from api.v2.obj_views.user_api import *
from api.v2.obj_views.history_api import *
from api.v2.obj_views.exprecn_api import *