import streamlit as st
import numpy as np
import pickle
import os

# Page config
st.set_page_config(page_title="Mobile Price Predictor", page_icon="📱")

# Title
st.title("📱 Mobile Phone Price Predictor (₹)")
st.markdown("Estimate the market price of a smartphone in **Indian Rupees (INR)** based on its hardware specs.")

# Debug (optional)
# st.write("Files available:", os.listdir())

# Load the trained model
try:
    with open("mobile_price_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file not found. Make sure 'mobile_price_model.pkl' is in the same folder as app.py.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Input fields
ram = st.slider("RAM (GB)", 2, 16, 6, step=1)
storage = st.slider("Storage (GB)", 32, 512, 128, step=32)
screen_size = st.slider("Screen Size (inches)", 4.5, 7.0, 6.5, step=0.1)
camera = st.slider("Main Camera (MP)", 8.0, 108.0, 48.0, step=1.0)
battery = st.slider("Battery Capacity (mAh)", 2000, 6000, 4000, step=100)

# Predict button
if st.button("Predict Price"):
    features = np.array([[ram, storage, screen_size, camera, battery]])
    try:
        usd_price = model.predict(features)[0]
        inr_price = usd_price * 83  # Fixed conversion rate

        # Format with Indian commas
        formatted_price = f"₹{inr_price:,.0f}".replace(",", ",")

        st.success(f"💰 Estimated Price: **{formatted_price}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")



