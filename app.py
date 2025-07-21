import streamlit as st
import pandas as pd
import pickle
import gdown
import pickle
import os

# Google Drive file ID
url = "https://drive.google.com/file/d/1yytE-KlfFsaMPTRxqOJvOTUntHERNTO8/view?usp=sharing"
output = "crop_yield_model.pkl"

# Download only if not already downloaded
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# Load the model
with open(output, "rb") as f:
    model = pickle.load(f)


# -------------------------
# Custom CSS Styling
# -------------------------
def add_bg_and_style():
    background_image_url = "https://satpalda.com/wp-content/uploads/2024/03/crop-yield-prediction-.png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}

        label, .stSelectbox div, .stSlider{{
            color: #000 !important;
            font-size: 16px;
        }}
        .stTextInput, .stSelectbox, .stNumberInput, .stSlider , .stRadio{{
            background-color: white !important;
        }}
        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            font-size: 16px;
            font-weight: bold;
        }}

        .stForm{{
            background-color: #e8f5e9 !important;
        }}

        .prediction-box {{
            background-color: #dcedc8;
            padding: 20px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            color: #33691e;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 20px;
        }}


        </style>
        """,
        unsafe_allow_html=True
    )
    

# -------------------------
# Load Trained Model
# -------------------------
with open("crop_yield_model.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------------
# Page Config and Styling
# -------------------------
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")
add_bg_and_style()

# -------------------------
# Title Section
# -------------------------
st.markdown("<h1 style='text-align: center; color:#33333;'>🌾 Crop Yield Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#33333;'>Estimate the crop yield (in tons/hectare) based on real farming conditions.</p>", unsafe_allow_html=True)

# -------------------------
# Input Form
# -------------------------
with st.container():
    st.markdown('<div class="form-style">', unsafe_allow_html=True)

    with st.form("input_form",height=400):
        st.markdown("### 📝 Enter Details")
        soil = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay", "Silty"])
        crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize", "Barley"])
        weather = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
        fertilizer = st.radio("Fertilizer Used?", ["Yes", "No"])
        irrigation = st.radio("Irrigation Used?", ["Yes", "No"])
        rainfall = st.slider("Rainfall (mm)", 0, 500, 100)
        temp = st.slider("Temperature (°C)", 0, 50, 25)
        days = st.slider("Days to Harvest", 30, 180, 90)

        submitted = st.form_submit_button("Predict Yield")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Prediction Logic
# -------------------------
if submitted:
    input_data = pd.DataFrame({
        'Soil_Type': [soil],
        'Crop': [crop],
        'Weather_Condition': [weather],
        'Fertilizer_Used': [1 if fertilizer == 'Yes' else 0],
        'Irrigation_Used': [1 if irrigation == 'Yes' else 0],
        'Rainfall_mm': [rainfall],
        'Temperature_Celsius': [temp],
        'Days_to_Harvest': [days]
    })

    prediction = model.predict(input_data)[0]
    st.markdown(
        f"""
        <div class="prediction-box">
            🌱 Predicted Crop Yield: <b>{prediction:.2f} tons/hectare</b>
        </div>
        """,
        unsafe_allow_html=True
    )
    

# -------------------------
# Footer
# -------------------------
st.markdown("<p style='text-align: center; color: white;'>Made by: <b>CK14</b></p>", unsafe_allow_html=True)