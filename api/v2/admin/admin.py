from flask import Flask, jsonify, make_response, abort, request
from api.v2.admin import admin
from models.user import User
from models.history import UserHistory
from models import exprecn
from api.v2.auth.auth import JWTAuth, BasicAuth, Auth

auth = Auth()
bAuth = BasicAuth()
jAuth = JWTAuth()

@admin.route('/users', methods=['POST'], strict_slashes=False)
def create_admin():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'email' not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'password' not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)
    