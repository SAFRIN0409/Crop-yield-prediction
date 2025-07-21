# train_model.py
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load dataset
df = pd.read_csv("crop.csv")

# Features and target
X = df.drop(columns=['Yield_tons_per_hectare', 'Region'])
y = df['Yield_tons_per_hectare']

# Define column types
categorical_cols = ['Soil_Type', 'Crop', 'Weather_Condition']
boolean_cols = ['Fertilizer_Used', 'Irrigation_Used']
numeric_cols = ['Rainfall_mm', 'Temperature_Celsius', 'Days_to_Harvest']

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
    ('num', 'passthrough', boolean_cols + numeric_cols)
])

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("crop_yield_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as crop_yield_model.pkl")
