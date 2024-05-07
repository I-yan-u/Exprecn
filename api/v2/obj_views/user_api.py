from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.user import User
from models.engine.image_processor import process_image
from datetime import datetime
from api.v2.auth.auth import Auth, BasicAuth, JWTAuth

auth = Auth()
bAuth = BasicAuth()
jAuth = JWTAuth()


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
    try:
        new_user = auth.register_user(**data)
        return make_response(jsonify(new_user.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'message': 'User Already exsit'}), 403)

@app_view.route('/users/<id>', methods=['PUT'], strict_slashes=False)
def update_user(id):
    """ Update user information"""
    time_now = datetime.utcnow()
    specific_user = store.get(User, id)
    if specific_user is None:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for k, v in data.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(specific_user, k, v)
    setattr(specific_user, 'updated_at', time_now)
    store.save()
    return make_response(jsonify(specific_user.to_dict()), 201)

@app_view.route('/users/image/<id>', methods=['PUT'], strict_slashes=False)
def user_image(id):
    """user API route to handle file upload
    """
    time_now = datetime.utcnow()
    specific_user = store.get(User, id)
    if specific_user is None:
        abort(404)

    client_image = request.files.get('image', None)
    if not client_image:
        return make_response(jsonify({"error": "Missing image"}), 400)
    
    try:
        image_data, image_size = process_image(client_image)
        if image_size > 1024:
            return make_response(jsonify({"error": "Image size too large"}), 400)
        setattr(specific_user, 'image', image_data)
        setattr(specific_user, 'updated_at', time_now)
        store.save()
        return make_response(jsonify({"massage": "Image upload success"}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "Server Error"}), 500)


    
    