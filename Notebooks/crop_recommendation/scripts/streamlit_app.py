import streamlit as st
import numpy as np
import joblib
import os

# Specify the custom save path for models and scalers
custom_save_path = 'Notebooks\crop_recommendation\models'  
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

# Define the input fields for the features
st.title('Crop Recommendation System')

st.write("Please input the following features:")

# Input fields for the selected features
n = st.number_input('Nitrogen (N)', value=0.0)
p = st.number_input('Phosphorus (P)', value=0.0)
k = st.number_input('Potassium (K)', value=0.0)
temperature = st.number_input('Temperature (°C)', value=0.0)
humidity = st.number_input('Humidity (%)', value=0.0)
ph  = st.number_input('PH', value=0.0)
rainfall = st.number_input('Rainfall (mm)', value=0.0)

# Create a feature vector from the input
features = np.array([[n, p, k, temperature, humidity,ph ,rainfall]])

# Scale the input features using the loaded feature scaler
features_scaled = feature_scaler.transform(features)

# Predict the crop type using all models
if st.button('Predict Crop Type'):
    st.write('Predictions:')
    for model_name, model in models.items():
        prediction = model.predict(features_scaled)[0]  # Get the predicted class
        
        # Display the predicted class
        st.write(f'{model_name}: {prediction}')
