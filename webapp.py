import streamlit as st
import pandas as pd
import pickle

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Define the prediction function
def predict_yield(Crop_Type, Farm_Area, Irrigation_Type, Fertilizer_Used, Pesticide_Used, Soil_Type, Season, Water_Usage):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        'Crop_Type': [Crop_Type],
        'Farm_Area': [Farm_Area],
        'Irrigation_Type': [Irrigation_Type],
        'Fertilizer_Used': [Fertilizer_Used],
        'Pesticide_Used': [Pesticide_Used],
        'Soil_Type': [Soil_Type],
        'Season': [Season],
        'Water_Usage': [Water_Usage]
    })

    # Predict yield using the loaded model
    yield_prediction = loaded_model.predict(input_data)[0]
    return yield_prediction

# Streamlit UI
st.title("Crop Yield (tons) Predictor")

# Input fields for the features
crop_type = st.selectbox("Select Crop Type", ["Wheat", "Rice", "Corn", "Soybeans", "Others"])  # Update options as needed
farm_area = st.number_input("Farm Area (in acres)", min_value=0.1, max_value=10000.0, value=1.0)
irrigation_type = st.selectbox("Select Irrigation Type", ["Drip", "Sprinkler", "Flood", "Rain-fed"])
fertilizer_used = st.number_input("Fertilizer Used (in tons)", min_value=0.0, max_value=1000.0, value=0.0)
pesticide_used = st.number_input("Pesticide Used (in kg)", min_value=0.0, max_value=1000.0, value=0.0)
soil_type = st.selectbox("Select Soil Type", ["Sandy", "Clay", "Loamy", "Silty"])
season = st.selectbox("Select Season", ["Spring", "Summer", "Autumn", "Winter"])
water_usage = st.number_input("Water Usage (in cubic meters)", min_value=0.0, max_value=100000.0, value=0.0)

# Button to make prediction
if st.button("Predict Yield"):
    result = predict_yield(crop_type, farm_area, irrigation_type, fertilizer_used, pesticide_used, soil_type, season, water_usage)
    st.success(f"Predicted Yield: {result:.2f} tons")

    