from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Specify the custom save path for models and scalers
custom_save_path = 'Notebooks/crop_recommendation/models'  
feature_scaler_filename = os.path.join(custom_save_path, 'feature_scaler.pkl')

# Load the scaler
feature_scaler = joblib.load(feature_scaler_filename)

# Load all the models
model_filenames = ['lightgbm.pkl', 'random_forest.pkl', 'support_vector_machine.pkl', 'neural_network.pkl', 'naive_bayes.pkl']
models = {}

for filename in model_filenames:
    model_name = filename.split('.')[0].replace('_', ' ').title()  # Extract model name
    model_path = os.path.join(custom_save_path, filename)
    models[model_name] = joblib.load(model_path)

# Define a route for predicting crop type
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.json
    # Extract features from the JSON data
    try:
        n = data['N']
        p = data['P']
        k = data['K']
        temperature = data['temperature']
        humidity = data['humidity']
        ph = data['ph']
        rainfall = data['rainfall']
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400

    # Create a feature vector
    features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
    
    # Scale the input features
    features_scaled = feature_scaler.transform(features)
    
    # Predict with each model
    predictions = {}
    for model_name, model in models.items():
        prediction = model.predict(features_scaled)[0]
        predictions[model_name] = prediction

    # Return the predictions as a JSON response
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
