import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Uber Fare Prediction",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🚕 Uber Fare Amount Prediction")
st.markdown("""
This application predicts the **fare amount** for Uber rides using Machine Learning (Regression Analysis).
Built with RandomForest model trained on historical Uber trip data.
""")

# Sidebar
st.sidebar.header("About")
st.sidebar.info("""
**Model Details:**
- Algorithm: Random Forest Regressor
- Features: 8 input parameters
- Target: Fare Amount (USD)
""")

# Load model and scaler
@st.cache_resource
def load_model():
    try:
        model = joblib.load('models/uber_fare_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        st.info("🔄 Training model for the first time... Please wait!")
        # Train the model
        try:
            import subprocess
            subprocess.run(['python', 'train_model.py'], check=True)
            model = joblib.load('models/uber_fare_model.pkl')
            scaler = joblib.load('models/scaler.pkl')
            st.success("✅ Model trained successfully!")
            return model, scaler
        except Exception as e:
            st.error(f"❌ Error training model: {str(e)}")
            return None, None

model, scaler = load_model()

if model is not None and scaler is not None:
    st.success("✅ Model loaded successfully!")
    
    # Main prediction section
    st.header("🎯 Make a Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Date & Time")
        pickup_month = st.slider("Month", 1, 12, 6)
        pickup_day = st.slider("Day of Month", 1, 31, 15)
        pickup_hour = st.slider("Hour of Day", 0, 23, 12)
    
    with col2:
        st.subheader("👥 Trip Details")
        passenger_count = st.number_input("Number of Passengers", 1, 6, 1)
    
    st.subheader("📍 Pickup Location")
    col3, col4 = st.columns(2)
    with col3:
        pickup_latitude = st.number_input("Pickup Latitude", -90.0, 90.0, 40.7128)
        pickup_longitude = st.number_input("Pickup Longitude", -180.0, 180.0, -74.0060)
    
    st.subheader("📍 Dropoff Location")
    col5, col6 = st.columns(2)
    with col5:
        dropoff_latitude = st.number_input("Dropoff Latitude", -90.0, 90.0, 40.7580)
        dropoff_longitude = st.number_input("Dropoff Longitude", -180.0, 180.0, -73.9855)
    
    # Prediction
    if st.button("🚀 Predict Fare", use_container_width=True):
        # Prepare input
        input_data = np.array([[
            pickup_month,
            pickup_day,
            pickup_hour,
            passenger_count,
            pickup_longitude,
            pickup_latitude,
            dropoff_longitude,
            dropoff_latitude
        ]])
        
        # Scale input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Display result
        st.markdown("---")
        st.subheader("💰 Predicted Fare Amount")
        
        col_result1, col_result2, col_result3 = st.columns(3)
        with col_result1:
            st.metric(
                label="Base Fare Prediction",
                value=f"${prediction:.2f}",
                delta=None
            )
        with col_result2:
            estimated_min = prediction * 0.9
            st.metric(
                label="Estimated Min",
                value=f"${estimated_min:.2f}"
            )
        with col_result3:
            estimated_max = prediction * 1.1
            st.metric(
                label="Estimated Max",
                value=f"${estimated_max:.2f}"
            )
        
        # Additional info
        st.info(f"""
        **Trip Summary:**
        - **Date:** Month {pickup_month}, Day {pickup_day}
        - **Time:** {pickup_hour}:00
        - **Passengers:** {int(passenger_count)}
        - **From:** ({pickup_latitude:.4f}, {pickup_longitude:.4f})
        - **To:** ({dropoff_latitude:.4f}, {dropoff_longitude:.4f})
        """)
        
        st.success(f"✅ Predicted fare amount: **${prediction:.2f}** (USD)")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: gray; font-size: 12px;">
        © 2024 Uber Fare Prediction App | Built with Streamlit & Scikit-Learn
    </div>
    """, unsafe_allow_html=True)
else:
    st.error("Cannot proceed without model files.")
