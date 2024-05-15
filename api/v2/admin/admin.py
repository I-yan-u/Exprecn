from flask import Flask, jsonify, make_response, abort, request
from api.v2.admin import admin
from models.engine.validators import email_validator
from models.user import User
from models.history import UserHistory
from models import exprecn
from api.v2.auth.auth import JWTAuth, BasicAuth, Auth

auth = Auth()
bAuth = BasicAuth()
jAuth = JWTAuth()

@admin.route('/create_admin', methods=['POST'], strict_slashes=False)
def create_admin():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'email' not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'password' not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)
    if 'first_name' not in data:
        return make_response(jsonify({"error": "Missing First name"}), 400)
    if 'last_name' not in data:
        return make_response(jsonify({"error": "Missing Last name"}), 400)
    
    if not email_validator(data['email']):
        return make_response(jsonify({"error": "Invalid email"}), 400)
    # if not pass_validator(data['password']):
    #     return make_response(jsonify({"error": "Invalid password", 
    #     "message": "Password should contain an Upper case, Lower case, \
    #     numerical and special character, must be 8 characters long e.g StrongPassword123!"}), 400)
    