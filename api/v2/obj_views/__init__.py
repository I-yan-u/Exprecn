#!/usr/bin/python3
from flask import Blueprint

app_view = Blueprint('app_view', __name__, url_prefix='/exprecn')
app_view.secret_key = 'b0a747d7-c9aa-434c-80fb-2cc4360d0bc7'

from api.v2.obj_views.index import *
from api.v2.obj_views.user_api import *
from api.v2.obj_views.history_api import *
from api.v2.obj_views.exprecn_api import *