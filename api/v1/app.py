#!/usr/bin/python3
"""
API version 1.0.0
"""
from flask import Flask, make_response, jsonify
from api.v1.obj_views import app_view
from models import store
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_view)
CORS(app)

@app.teardown_appcontext
def db_close(exception=None):
    """ close the database """
    store.close()

@app.errorhandler(404)
def error_404(error):
    """404 error handler"""
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)
