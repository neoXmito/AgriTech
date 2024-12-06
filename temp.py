# AgriTech: Agricultural Intelligence Solution

## Overview

AgriTech is an advanced machine learning-powered application designed to provide innovative solutions for agricultural challenges. By leveraging cutting-edge technologies, we aim to support farmers with intelligent, data-driven insights.

## Project Description

AgriTech addresses critical agricultural needs through three key functionalities:
- Crop Recommendation
- Field Production Prediction
- Plant Disease Recognition

## Technologies Stack

### Machine Learning
- **Frameworks**: TensorFlow, Scikit-learn
- **Data Sources**: 
  - Plant Village
  - Roboflow

### Web Technologies
- **Backend**: Node.js
- **Frontend**: 
  - React
  - React Native

## Key Features

### 1. Crop Recommendation System

#### Features Used
- **N**: Nitrogen content in soil (kg/ha)
- **P**: Phosphorous content in soil (kg/ha)
- **K**: Potassium content in soil (kg/ha)
- **Temperature**: Ambient temperature (°C)
- **Humidity**: Humidity rate (%)
- **pH**: Soil pH level
- **Rainfall**: Precipitation amount (mm)

#### Machine Learning Models Tested
- LightGBM
- Random Forest
- Support Vector Machine
- Neural Network
- Naïve Bayes

**Best Performing Model**: Naïve Bayes with 99% accuracy

### 2. Field Production Prediction

#### Features Used
- **Area**: Cultivated surface (hectares)
- **Item**: Type of crop or agricultural product
- **Year**: Production year
- **Yield**: Yield per hectare (hectograms)
- **Average Rainfall**: Annual average rainfall (mm)
- **Pesticides**: Quantity of pesticides used (tonnes)
- **Average Temperature**: Mean temperature (°C)

#### Machine Learning Models Tested
- Linear Regression
- Lasso
- Ridge
- K-Nearest Neighbors
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting
- XGBoost

**Best Performing Model**: Random Forest Regressor
- Mean Squared Error (MSE): 9892.72
- R² Score: 0.9867

### 3. Plant Disease Recognition and Treatment Recommendation

#### Disease Recognition
- **Model**: YOLOv5
- Trained on diverse agricultural disease datasets
- Precise disease classification from plant images

#### Treatment Recommendation
- Natural Language Processing (NLP) approach
- Advanced models used:
  - Llama 3.1 (70B-versatile) for text data processing
  - Groc for response optimization

## Installation

### Prerequisites
- Node.js (v14+)
- npm or yarn
- Python (3.7+)
- TensorFlow
- Scikit-learn

### Setup Steps
1. Clone the repository
   ```bash
   git clone https://github.com/your-username/agritech.git
   cd agritech
   ```

2. Install backend dependencies
   ```bash
   cd backend
   npm install
   ```

3. Install frontend dependencies
   ```bash
   cd ../frontend
   npm install
   ```

4. Setup machine learning environment
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
```bash
# Start backend
cd backend
npm run dev

# Start frontend
cd ../frontend
npm start
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Lead: [Your Name]
Email: contact@agritech.com
Project Link: [https://github.com/your-username/agritech](https://github.com/your-username/agritech)

## Acknowledgments
- Plant Village
- Roboflow
- TensorFlow Community
- Open-source contributors

---

**Note**: This project is actively under development. Contributions and feedback are welcome!