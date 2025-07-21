# 🌾 Crop Yield Prediction System

This web-based Crop Yield Prediction System allows users to estimate crop yield (in tons/hectare) using machine learning based on real-time agricultural inputs like rainfall, temperature, soil type, crop type, and more.

Built with **Python**, **Streamlit**, and a **trained Random Forest model**, the app is designed for farmers, researchers, and agritech enthusiasts to help make informed decisions.

---

## 🔗 Live Demo

👉 Try it here: [https://crop-yield-prediction-safrin0431.streamlit.app/]

---
## 📌 Features

- 🌦️ Input agricultural data: Soil type, crop, weather, rainfall, temperature, fertilizer use, and irrigation.
- 🤖 Predicts crop yield instantly using a trained machine learning model.
- 💻 Clean and responsive web UI using Streamlit.
- 📊 Visual design with styled components and background image.

---

## 🧠 Machine Learning Model

- **Model Used**: Random Forest Regressor
- **Trained On**: Synthetic/sample agricultural data with the following features:
  - `Soil_Type`
  - `Crop`
  - `Weather_Condition`
  - `Fertilizer_Used`
  - `Irrigation_Used`
  - `Rainfall_mm`
  - `Temperature_Celsius`
  - `Days_to_Harvest`

---

## 📁 Project Structure

```
crop-yield-prediction/
├── app.py                  # Streamlit main app
├── crop_yield_model.pkl    # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAFRIN0409/Crop-yield-prediction.git
   cd crop-yield-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📦 Dependencies

- streamlit
- pandas
- scikit-learn

You can install them all via:

```bash
pip install -r requirements.txt
```

---

## 📸 App Preview

st.image(""C:\Users\Safrin\Pictures\Screenshots\Screenshot 2025-07-21 102114.png"", width=150, caption="Created by SAFRIN M")

---

## 👨‍💻 Author

SAFRIN M  
Built with ❤️ using Python & Streamlit  
Connect on [https://www.linkedin.com/in/safrin0409](https://www.linkedin.com/) | [GitHub](https://github.com/SAFRIN0409)
