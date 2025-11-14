from . import api_bp
from services.prediction import get_prediction
from flask import request, jsonify

@api_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Not picked any file'}), 400

    try:
        img_bytes = file.read()
        result_data = get_prediction(img_bytes)
        return jsonify(result_data)

    except ValueError as err: 
        return jsonify({'error': str(err)}), 500
    except Exception as err:
        return jsonify({'error': f'Server erorr: {str(err)}'}), 500