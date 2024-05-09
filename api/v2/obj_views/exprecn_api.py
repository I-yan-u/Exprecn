from models.exprecn import Exprecn
from models.engine.codon_maker import clean_seq, codons_gen
from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.user import User
from models.history import UserHistory
from api.v2.auth.auth import JWTAuth

jauth = JWTAuth()

def split_res(str):
    res_str = ' '
    split_res = codons_gen(str)
    return res_str.join(split_res)

@app_view.route('/run', methods=['POST'], strict_slashes=False)
def run():
    """Exprecn api run without user authentication"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'action' not in data:
        return make_response(jsonify({"error": "Missing action"}), 400)
    if 'query' not in data:
        return make_response(jsonify({"error": "Missing Sequence"}), 400)
    
    query = clean_seq(data['query'])
    action = data['action']
    express = Exprecn(query)
    result_obj = {'action': action, 'obj': express.to_dict() ,'result': ''}

    if data['query'] == '' or data['query'] == None:
        result_obj['result'] = None
        return jsonify(result_obj)
    else:
        if action == 'transcribe':
            result = express.transcribe()
            result_obj['result'] = result
        if action == 'translate':
            result = express.translate()
            result_obj['result'] = result
        return jsonify(result_obj)

@jauth.token_required
@app_view.route('/run/user', methods=['POST'], strict_slashes=False)
def user_run(id):
    """Exprecn api run with user authentication"""
    user = store.get(User, id)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'action' not in data:
        return make_response(jsonify({"error": "Missing action"}), 400)
    if 'query' not in data:
        return make_response(jsonify({"error": "Missing Sequence"}), 400)
    if user == None:
        return make_response(jsonify({"error": "User Id not found"}), 400)
    
    history_obj = {
        'action': data['action'],
        'query': split_res(clean_seq(data['query'])),
        'user_id': user.id,
        'result': ''
    }
    
    query = clean_seq(data['query'])
    action = data['action']
    express = Exprecn(query)
    result_obj = {'action': action, 'obj': express.to_dict() ,'result': ''}

    if data['query'] == '' or data['query'] == None:
        result_obj['result'] = None
        return jsonify(result_obj)
    else:
        if action == 'transcribe':
            result = express.transcribe()
            result_obj['result'] = result
            history_obj['result'] = str(result)
        if action == 'translate':
            result = express.translate()
            result_obj['result'] = result
            history_obj['result'] = str(result)

        history = UserHistory(**history_obj)
        store.new(history)
        store.save()
        return jsonify(result_obj)
