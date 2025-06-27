import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("mobile_price_model.pkl", "rb"))

# Title
st.title("📱 Mobile Phone Price Predictor")

# Input sliders
ram = st.slider("RAM (GB)", 2, 16, step=1)
storage = st.slider("Storage (GB)", 32, 512, step=32)
screen_size = st.slider("Screen Size (inches)", 4.5, 7.0, step=0.1)
camera = st.slider("Camera (MP)", 8.0, 108.0, step=1.0)
battery = st.slider("Battery Capacity (mAh)", 2000, 6000, step=100)

# Predict button
if st.button("Predict Price"):
    features = np.array([[ram, storage, screen_size, camera, battery]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: ${prediction[0]:.2f}")
