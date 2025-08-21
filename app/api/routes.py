import time
import random
from flask import Blueprint, request, jsonify

# Blueprint Configuration
api = Blueprint(
    'api', __name__,
    template_folder='../templates',
    static_folder='../static'
)

@api.route('/predict', methods=['POST'])
def predict():
    """
    Receives email text from the frontend and returns a simulated prediction.
    """
    try:
        data = request.get_json()
        email_text = data['email_text']

        if not email_text or not email_text.strip():
             return jsonify({'error': 'Email text cannot be empty.'}), 400

        # Simulate model processing time
        time.sleep(1) 

        # --- DUMMY MODEL LOGIC ---
        # Replace this with your actual model prediction later
        predictions = ['spam', 'not spam']
        result = random.choice(predictions)
        # -------------------------

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500