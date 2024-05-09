from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.user import User
from models.engine.image_processor import process_image
from datetime import datetime, timedelta
from api.v2.auth.auth import Auth, BasicAuth, JWTAuth

auth = Auth()
bAuth = BasicAuth()
jAuth = JWTAuth()

@app_view.route('/login', methods=['GET'], strict_slashes=False)
def login():
    if bAuth.validate(request):
        user = bAuth.current_user(request)
        payload = {
            'email': user.email,
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=60)
        }
        token = jAuth.encode_token(payload)
        return jsonify({'token': token, 'id': user.id})
    return make_response(jsonify({'message': 'Login Failed'}), 401)


@app_view.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Returns all users"""
    all_obj = store.all(User)
    _all_users = [obj.to_dict() for obj in all_obj.values()]
    return jsonify(_all_users)


@app_view.route('/user', methods=['GET'], strict_slashes=False)
@jAuth.token_required
def user(user):
    """Returns specific user"""
    if user is None:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)
    return jsonify(user.to_dict())

@app_view.route('/users/', methods=['DELETE'], strict_slashes=False)
@jAuth.token_required
def del_user(user):
    """Deletes a user information"""
    if user is None:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)
    store.delete(user)
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

@app_view.route('/users', methods=['PUT'], strict_slashes=False)
@jAuth.token_required
def update_user(user):
    """ Update user information"""
    time_now = datetime.utcnow()
    if user is None:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for k, v in data.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(user, k, v)
    setattr(user, 'updated_at', time_now)
    store.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_view.route('/users/image', methods=['PUT'], strict_slashes=False)
@jAuth.token_required
def user_image(user):
    """user API route to handle file upload
    """
    time_now = datetime.utcnow()
    if user is None:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)

    client_image = request.files.get('image', None)
    if not client_image:
        return make_response(jsonify({"error": "Missing image"}), 400)
    
    try:
        image_data, image_size = process_image(client_image)
        if image_size > 1024:
            return make_response(jsonify({"error": "Image size too large"}), 400)
        setattr(user, 'image', image_data)
        setattr(user, 'updated_at', time_now)
        store.save()
        return make_response(jsonify({"massage": "Image upload success"}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "Server Error"}), 500)


    
    