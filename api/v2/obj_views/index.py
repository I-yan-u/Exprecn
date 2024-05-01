from flask import Flask, jsonify, make_response
from api.v2.obj_views import app_view
import models
from models.user import User
from models.history import UserHistory

classes = {'User': User, 'UserHistory': UserHistory}

obj = {
    'User': models.store.count(User),
    'UserHistory': models.store.count(UserHistory)
}

@app_view.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({'status': 'OK😁', 'code': 200})

@app_view.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns stats"""
    return jsonify(obj)