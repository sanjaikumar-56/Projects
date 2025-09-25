import streamlit as st
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("lasso_model")
scaler = joblib.load("scaler")

# App title
st.title(":green[House] Price Predictor :house:")

# User Inputs
bedrooms = st.number_input('Bedrooms', min_value=1, max_value=10, step=1)
bathrooms = st.number_input('Bathrooms', min_value=1.0, max_value=10.0, step=0.5)
sqft_living = st.number_input('Living Area (sqft)', min_value=500, max_value=10000, step=100)
floors = st.number_input('Floors', min_value=1.0, max_value=3.0, step=0.5)
yr_built = st.number_input('Year Built', min_value=1900, max_value=2023, step=1)

# Predict button
if st.button("Predict Price"):
    # Match input format used in model training
    input_data = np.array([[bedrooms, bathrooms, sqft_living, floors, yr_built]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Output
    st.success(f"💰 Estimated House Price: $ {round(prediction[0], 2)}")
