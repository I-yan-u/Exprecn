from models.exprecn import Exprecn
from models.engine.codon_maker import clean_seq
from flask import Flask, jsonify, make_response, abort, request
from api.v1.obj_views import app_view
from models import store

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

    if action == 'transcribe':
        result = express.transcribe()
        result_obj['result'] = result
    if action == 'translate':
        result = express.translate()
        result_obj['result'] = result
    return jsonify(result_obj)


    
