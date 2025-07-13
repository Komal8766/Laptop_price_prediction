import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("laptop_price_model.pkl")  # Ensure this file exists

# Title and UI
st.set_page_config(page_title="💻Laptop Price Predictor", page_icon="💻")
st.title("💻 Laptop Price Prediction App")

# Input fields
brand = st.selectbox("Brand", ['Asus', 'Acer', 'Lenovo', 'HP', 'Dell', 'Apple'])
processor_speed = st.slider("Processor Speed (GHz)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)
ram = st.selectbox("RAM Size (GB)", [4, 8, 16, 32, 64])
storage = st.selectbox("Storage Capacity (GB)", [128, 256, 512, 1000, 2000])
screen_size = st.slider("Screen Size (inches)", min_value=10.0, max_value=18.0, value=13.3, step=0.1)
weight = st.slider("Weight (kg)", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

# Map brand to encoded value
brand_map = {'Acer': 0, 'Apple': 1, 'Asus': 2, 'Dell': 3, 'HP': 4, 'Lenovo': 5}
brand_encoded = brand_map[brand]

# Feature vector
features = np.array([[brand_encoded, processor_speed, ram, storage, screen_size, weight]])

# Predict
if st.button("Predict Price"):
    price = model.predict(features)[0]
    st.success(f"💰 Estimated Laptop Price: ₹{price:,.2f}")