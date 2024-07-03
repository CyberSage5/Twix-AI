# backend/app/routes/example.py
from flask import jsonify
from . import bp

@bp.route('/api/example', methods=['GET'])
def example_api():
    data = {
        'message': 'Hello from Twix AI Backend!'
    }
    return jsonify(data)
