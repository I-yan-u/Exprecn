from datetime import datetime, timedelta
from flask import Flask, jsonify, make_response, abort, request
from api.v2.admin import admin
from models.engine.validators import email_validator
from models.user import User
from models.history import UserHistory
from models import exprecn, store
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
    try:
        data['admin'] = 1
        new_user = auth.register_user(**data)
        return make_response(jsonify(new_user.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'message': 'User Already exsit'}), 403)
    
@admin.route('/login', methods=['GET'], strict_slashes=False)
def login():
    if bAuth.validate(request):
        user = bAuth.current_user(request)
        payload = {
            'email': user.email,
            'id': user.id,
            'admin': user.admin,
            'exp': datetime.utcnow() + timedelta(minutes=60)
        }
        token = jAuth.encode_token(payload)
        return jsonify({'token': token, 'id': user.id, 'admin': bool(user.admin)})
    return make_response(jsonify({'message': 'Login Failed'}), 401)

@admin.route('/history', methods=['GET'], strict_slashes=False)
@jAuth.admin_token
def admin_get_history(admin):
    """Get user history"""
    if not admin:
        abort(403)
    return jsonify(store.all(UserHistory))


@admin.route('/users', methods=['GET'], strict_slashes=False)
@jAuth.admin_token
def admin_get_user(admin):
    """Get user history"""
    if not admin:
        abort(403)
    return jsonify(store.all(User))


@admin.route('/users', methods=['DELETE'], strict_slashes=False)
@jAuth.admin_token
def admin_delete_user(admin):
    """Get user history"""
    if not admin:
        abort(403)
    try:
        userId = request.args.get('userId')
        user = store.get_users(userId)
        user.delete()
        return make_response(jsonify({}), 200)
    except Exception:
        abort(404)


@admin.route('/history', methods=['DELETE'], strict_slashes=False)
@jAuth.admin_token
def admin_delete_history(admin):
    """Get user history"""
    if not admin:
        abort(403)
    try:
        histId = request.args.get('histId')
        history = store.get_hist(histId)
        history.delete()
        return make_response(jsonify({}), 200)
    except Exception:
        abort(404)

    
@admin.route('/users', methods=['PUT'], strict_slashes=False)
@jAuth.admin_token
def admin_update_user(admin):
    """Get user history"""
    if not admin:
        abort(403)
    try:
        data = request.get_json()
        userId = data.get('userId')
        user = store.get_users(userId)
        user.update(data)
        return make_response(jsonify(user.to_dict()), 200)
    except Exception:
        abort(404)