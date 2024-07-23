from models.exprecn import Exprecn
from models.engine.codon_maker import clean_seq, codons_gen
from flask import Flask, jsonify, make_response, abort, request
from api.v2.obj_views import app_view
from models import store
from models.user import User
from models.history import UserHistory
from api.v2.auth.auth import JWTAuth
import json

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
    action = data['action'].lower()
    express = Exprecn(query)
    result_obj = {'action': action, 'obj': express.to_dict() ,'result': ''}

    if data['query'] == '' or data['query'] == None:
        result_obj['result'] = None
        return jsonify(result_obj)
    else:
        if action == 'transcribe':
            if 'reverseTranscribe' in data and data['reverseTranscribe'] == 'true':
                result = express.transcribe(reversed=True)
            else:
                result = express.transcribe()
            result_obj['result'] = result
            result_obj['options'] = {'reverseTranscribe': data.get('reverseTranscribe', 'false')}
        if action == 'translate':
            meth = data.get('methionine', True)
            ret = data.get('listView', True)
            meth = True if meth == True or (type(meth) == 'str' and meth.lower() == 'true') else False
            ret = 'list' if ret == True or (type(ret) == 'str' and ret.lower() == 'true') else 'string'
            result = express.translate(meth=meth, ret=ret)
            result_obj['result'] = result
            result_obj['options'] = {'methionine': meth, 'listView': ret}
        return jsonify(result_obj)


@app_view.route('/user/run', methods=['POST'], strict_slashes=False)
@jauth.token_required
def user_run(user):
    """Exprecn api run with user authentication"""
    if not user:
        return make_response(jsonify({"error": "User not found"}), 400)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'action' not in data:
        return make_response(jsonify({"error": "Missing action"}), 400)
    if 'query' not in data:
        return make_response(jsonify({"error": "Missing Sequence"}), 400)
    
    history_obj = {
        'action': data['action'].lower(),
        'query': split_res(clean_seq(data['query'])),
        'user_id': user.id,
        'result': '',
        'options': None
    }
    
    query = clean_seq(data['query'])
    action = data['action'].lower()
    express = Exprecn(query)
    result_obj = {'action': action, 'obj': express.to_dict(), 'result': ''}

    if data['query'] == '' or data['query'] == None:
        result_obj['result'] = None
        return jsonify(result_obj)
    else:
        if action == 'transcribe':
            if 'reverseTranscribe' in data and data['reverseTranscribe'] == 'true':
                result = express.transcribe(reversed=True)
            else:
                result = express.transcribe()
            result_obj['result'] = result
            result_obj['options'] = {'reverseTranscribe': data.get('reverseTranscribe', 'false')}
            history_obj['result'] = result
            history_obj['options'] = {'reverseTranscribe': data.get('reverseTranscribe', 'false')}
        if action == 'translate':
            meth = data.get('methionine', True)
            ret = data.get('listView', True)
            meth = True if meth == True or (type(meth) == 'str' and meth.lower() == 'true') else False
            ret = 'list' if ret == True or (type(ret) == 'str' and ret.lower() == 'true') else 'string'
            result = express.translate(meth=meth, ret=ret)
            result_obj['result'] = result
            result_obj['options'] = {'methionine': meth, 'listView': ret}
            history_obj['result'] = result
            history_obj['options'] = {'methionine': meth, 'listView': ret}

        history = UserHistory(**history_obj)
        history.save()
        return jsonify(result_obj)
