import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.pkl")

# App Title
st.title("🏠 House Price Prediction")

st.write("Enter the house details below to predict the price.")

# User Inputs
MedInc = st.number_input("Median Income", value=3.5)

HouseAge = st.number_input("House Age", value=25.0)

AveRooms = st.number_input("Average Rooms", value=5.0)

AveBedrms = st.number_input("Average Bedrooms", value=1.0)

Population = st.number_input("Population", value=1000.0)

AveOccup = st.number_input("Average Occupancy", value=3.0)

Latitude = st.number_input("Latitude", value=34.0)

Longitude = st.number_input("Longitude", value=-118.0)

# Prediction Button
if st.button("Predict Price"):

    features = np.array([[MedInc,
                          HouseAge,
                          AveRooms,
                          AveBedrms,
                          Population,
                          AveOccup,
                          Latitude,
                          Longitude]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ${prediction[0]*100000:.2f}")