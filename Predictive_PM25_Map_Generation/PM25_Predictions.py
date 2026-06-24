# ==========================================================
# AQIVision Project
# Script 17
# Generate PM2.5 Predictions Using Saved Random Forest Model
# ==========================================================

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("AQIVision - Generate PM2.5 Predictions")
print("=" * 60)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_excel(
    r"C:\Users\jayam\Downloads\AQIVision_Final_Dataset_With_Coordinates.xlsx"
)

print("\nDataset Loaded Successfully")
print("Shape :", df.shape)

# ----------------------------------------------------------
# Create Date Features
# ----------------------------------------------------------

df["Month"] = pd.to_datetime(df["Month"])

df["Year"] = df["Month"].dt.year
df["Month_Num"] = df["Month"].dt.month
df["Day"] = 1

# ----------------------------------------------------------
# Calculate Wind Speed
# ----------------------------------------------------------

if "WindSpeed" not in df.columns:
    df["WindSpeed"] = np.sqrt(df["U10M"]**2 + df["V10M"]**2)

# ----------------------------------------------------------
# Encode City
# ----------------------------------------------------------

encoder = LabelEncoder()

df["City_Encoded"] = encoder.fit_transform(df["City"])

print("\nCity Encoding Completed")

# ----------------------------------------------------------
# Features Used During Training
# ----------------------------------------------------------

features = [

    "City_Encoded",
    "Year",
    "Month_Num",
    "Day",

    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",

    "AOD_550",

    "T2M",
    "QV2M",
    "PS",
    "PBLTOP",

    "WindSpeed"

]

X = df[features]

# ----------------------------------------------------------
# Load Saved Model
# ----------------------------------------------------------

model = joblib.load(
    r"C:\Users\jayam\Downloads\AQIVision_RF_Model.pkl"
)

print("\nRandom Forest Model Loaded Successfully")

# ----------------------------------------------------------
# Generate Predictions
# ----------------------------------------------------------

df["Predicted_PM25"] = model.predict(X)

print("\nPredictions Generated Successfully")

# ----------------------------------------------------------
# Save Prediction Dataset
# ----------------------------------------------------------

output_path = (
    r"C:\Users\jayam\Downloads\AQIVision_PM25_Predictions.xlsx"
)

df.to_excel(
    output_path,
    index=False
)

print("\nPrediction Dataset Saved Successfully")

print(output_path)

print("\nSample Predictions")

print(df[
    ["City",
     "PM2.5",
     "Predicted_PM25"]
].head())

print("\nDone.")
