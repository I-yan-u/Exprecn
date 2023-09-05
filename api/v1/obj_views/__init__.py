#!/usr/bin/python3
from flask import Blueprint

app_view = Blueprint('app_view', __name__, url_prefix='/api/v1')

from api.v1.obj_views.index import *
from api.v1.obj_views.user_api import *
from api.v1.obj_views.history_api import *
from api.v1.obj_views.exprecn_api import *