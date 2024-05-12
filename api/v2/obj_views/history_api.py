from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.history import UserHistory
from models.user import User
from api.v2.auth.auth import JWTAuth


jAuth = JWTAuth()


@app_view.route('/users/history', methods=['GET'], strict_slashes=False)
def all_user_history():
    """Returns all users"""
    all_obj = store.all(UserHistory)
    _all_user_history = [obj.to_dict() for obj in all_obj.values()]
    return jsonify(_all_user_history)

@app_view.route('/user/history', methods=['GET'], strict_slashes=False)
@jAuth.token_required
def user_history(user):
    """Returns specific user"""
    if not user:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)
    user_hist = []
    all_user_history = store.get_hist_user(user.id)
    if not all_user_history:
        return make_response(jsonify({'error': 'User history not found'}), 404)
    for hist in all_user_history:
        user_hist.append(hist.to_dict())
    return jsonify(user_hist)

@app_view.route('/user/history/id', methods=['GET'], strict_slashes=False)
@jAuth.token_required
def specific_user_history(user):
    """Returns specific user"""
    id = request.args.get('id')
    if not user:
        return make_response(jsonify({'error': 'Unauthorised'}), 401)
    spec_user_history = store.get_hist_user(user.id, id)
    if spec_user_history is None:
        return make_response(jsonify({'error': 'User history not found'}), 404)
    return jsonify(spec_user_history.to_dict())
 
@app_view.route('/users/<user_id>/history/<id>', methods=['DELETE'], strict_slashes=False)
def del_user_history(user_id, id):
    """Deletes a user information"""
    specific_hist = store.get_hist_user(user_id, id)
    if specific_hist is None:
        abort(404)
    store.delete(specific_hist)
    store.save()
    remaining_hist = []
    for hist in store.get_hist_user(user_id):
        remaining_hist.append(hist.to_dict())
    return jsonify(remaining_hist)

@app_view.route('/users/<user_id>/history', methods=['DELETE'], strict_slashes=False)
def del_all_user_history(user_id):
    """Deletes a user information"""
    user_history = store.get_hist_user(user_id)
    if user_history is None:
        abort(404)
    for hist in user_history:
        store.delete(hist)
    store.save()
    return jsonify({})

@app_view.route('/users/history', methods=['POST'], strict_slashes=False)
def create_user_history():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'action' not in data:
        return make_response(jsonify({"error": "Missing action"}), 400)
    if 'query' not in data:
        return make_response(jsonify({"error": "Missing Sequence"}), 400)
    if 'user_id' not in data:
        return make_response(jsonify({"error": "Missing User_id"}), 400)
    
    new_user_history = UserHistory(**data)
    store.new(new_user_history)
    store.save()
    return make_response(jsonify(new_user_history.to_dict()), 201)

@app_view.route('/users/history/<string:id>', methods=['PUT'], strict_slashes=False)
def update_user_history(id):
    """ Update user information"""
    specific_hist = store.get(UserHistory, id)
    if specific_hist is None:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for k, v in data.items():
        if k != 'id':
            setattr(specific_hist, k, v)
    store.save()
    return make_response(jsonify(specific_hist.to_dict()), 201)

    
    