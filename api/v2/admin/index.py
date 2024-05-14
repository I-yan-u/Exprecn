from flask import Flask, jsonify, make_response, abort, request
from api.v2.admin import admin
from models.user import User
from models.history import UserHistory
from models import exprecn
from api.v2.auth.auth import JWTAuth, BasicAuth, Auth

auth = Auth()
bAuth = BasicAuth()
jAuth = JWTAuth()

