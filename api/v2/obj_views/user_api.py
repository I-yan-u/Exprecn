from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.user import User
from PIL import Image

@app_view.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Returns all users"""
    all_obj = store.all(User)
    _all_users = [obj.to_dict() for obj in all_obj.values()]
    return jsonify(_all_users)

@app_view.route('/users/<string:id>', methods=['GET'], strict_slashes=False)
def user(id):
    """Returns specific user"""
    specific_user = store.get(User, id)
    if specific_user is None:
        abort(404)
    return jsonify(specific_user.to_dict())

@app_view.route('/users/<id>', methods=['DELETE'], strict_slashes=False)
def del_user(id):
    """Deletes a user information"""
    specific_user = store.get(User, id)
    if specific_user is None:
        abort(404)
    store.delete(specific_user)
    store.save()
    return jsonify({})

@app_view.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
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
    new_user = User(**data)
    store.new(new_user)
    store.save()
    return make_response(jsonify(new_user.to_dict()), 201)

@app_view.route('/users/<id>', methods=['PUT'], strict_slashes=False)
def update_user(id):
    """ Update user information"""
    specific_user = store.get(User, id)
    if specific_user is None:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for k, v in data.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(specific_user, k, v)
    store.save()
    return make_response(jsonify(specific_user.to_dict()), 201)

@app_view.route('/users/image/<id>', methods=['PUT'], strict_slashes=False)
def user_image(id):
    """_summary_
    """
    pass


    
    