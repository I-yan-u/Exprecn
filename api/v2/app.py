#!/usr/bin/python3
"""
API version 1.0.0
"""
from flask import Flask, make_response, jsonify
from api.v2.obj_views import app_view
from api.v2.admin import admin
from models import store
from flask_cors import CORS
from config import ENV
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_view)
app.register_blueprint(admin)
CORS(app, supports_credentials=True, origins=["http://0.0.0.0:5173", "http://127.0.0.1:5173",
                                              "http://localhost:5173"])
run_type = getenv('RUNSTAGE') or ENV['stage']


@app.teardown_appcontext
def db_close(exception=None):
    """ close the database """
    store.close()


@app.errorhandler(404)
def error_404(error):
    """404 error handler"""
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


# @app.before_request
# def 


if __name__ == '__main__':
    print('Running in', run_type, 'mode')
    app.run(debug=True, host=ENV['host'], port=ENV['port'], threaded=True)
