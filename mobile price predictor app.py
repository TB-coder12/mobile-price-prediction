import streamlit as st
import numpy as np
import pickle
import os

# Page setup
st.set_page_config(page_title="Mobile Price Predictor", page_icon="📱")

# App title
st.title("📱 Mobile Phone Price Predictor")
st.markdown("Predict the market price of a smartphone based on hardware specs.")

# Optional: Debugging file list
# st.write("📄 Files found:", os.listdir())

# Load the model
try:
    with open("mobile_price_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file not found. Make sure 'mobile_price_model.pkl' is in the same folder as app.py.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Input sliders
ram = st.slider("RAM (GB)", min_value=2, max_value=16, value=6, step=1)
storage = st.slider("Storage (GB)", min_value=32, max_value=512, value=128, step=32)
screen_size = st.slider("Screen Size (inches)", min_value=4.5, max_value=7.0, value=6.5, step=0.1)
camera = st.slider("Main Camera (MP)", min_value=8.0, max_value=108.0, value=48.0, step=1.0)
battery = st.slider("Battery Capacity (mAh)", min_value=2000, max_value=6000, value=4000, step=100)

# Predict button
if st.button("Predict Price"):
    features = np.array([[ram, storage, screen_size, camera, battery]])
    try:
        prediction = model.predict(features)
        st.success(f"💰 Estimated Price: **${prediction[0]:.2f}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")


