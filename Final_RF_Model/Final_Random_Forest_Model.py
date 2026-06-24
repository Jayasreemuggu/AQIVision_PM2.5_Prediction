# ==========================================================
# AQIVision Project
# Final Random Forest Model
#
# Includes:
# 1. Dataset Preparation
# 2. Feature Engineering
# 3. Random Forest Training
# 4. Performance Evaluation
# 5. Feature Importance Table
# 6. 5-Fold Cross Validation
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_excel(
    r"C:\Users\jayam\OneDrive\Desktop\AQI\AQI_Excel sheets\AQIVision_Final_Dataset3.xlsx"
)

print("="*60)
print("AQIVision Final Random Forest Model")
print("="*60)

# ----------------------------------------------------------
# Feature Engineering
# ----------------------------------------------------------

df["Month"] = pd.to_datetime(df["Month"])

df["Year"] = df["Month"].dt.year

df["Month_Num"] = df["Month"].dt.month

df["Day"] = 1

# ----------------------------------------------------------
# Label Encoding
# ----------------------------------------------------------

encoder = LabelEncoder()

df["City_Encoded"] = encoder.fit_transform(df["City"])

# ----------------------------------------------------------
# Features
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

target = "PM2.5"

X = df[features]

y = df[target]

# ----------------------------------------------------------
# Train Test Split
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ----------------------------------------------------------
# Random Forest
# ----------------------------------------------------------

rf = RandomForestRegressor(

    n_estimators=100,

    random_state=42

)

rf.fit(X_train,y_train)

# ----------------------------------------------------------
# Prediction
# ----------------------------------------------------------

y_pred = rf.predict(X_test)

# ----------------------------------------------------------
# Performance
# ----------------------------------------------------------

mae = mean_absolute_error(y_test,y_pred)

rmse = np.sqrt(

    mean_squared_error(y_test,y_pred)

)

r2 = r2_score(

    y_test,

    y_pred

)

print("\nModel Performance")

print("------------------------")

print("MAE  :",round(mae,2))

print("RMSE :",round(rmse,2))

print("R²   :",round(r2,3))

# ----------------------------------------------------------
# Feature Importance Table
# ----------------------------------------------------------

importance = pd.DataFrame({

    "Feature":features,

    "Importance":rf.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print("\nFeature Importance")

print("------------------------")

print(importance)

# ----------------------------------------------------------
# 5 Fold Cross Validation
# ----------------------------------------------------------

kf = KFold(

    n_splits=5,

    shuffle=True,

    random_state=42

)

cv_scores = cross_val_score(

    rf,

    X,

    y,

    cv=kf,

    scoring="r2"

)

print("\nCross Validation")

print("------------------------")

print("Individual R² Scores")

print(cv_scores)

print("\nMean R² :",round(cv_scores.mean(),3))

print("Std Dev :",round(cv_scores.std(),3))

print("\nFinal Random Forest Completed Successfully.")


# ==========================================================
# AQIVision Project
# Script: 13_Final_Feature_Importance.py
#
# Objective:
# Generate the Feature Importance plot for the
# Final Random Forest Model.
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Feature Importance DataFrame
# ----------------------------------------------------------

importance = pd.DataFrame({

    "Feature": features,

    "Importance": rf.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print(importance)

# ----------------------------------------------------------
# Plot Feature Importance
# ----------------------------------------------------------

plt.figure(figsize=(10,6))

bars = plt.barh(

    importance["Feature"],

    importance["Importance"],

    edgecolor="black"

)

plt.gca().invert_yaxis()

plt.xlabel("Feature Importance", fontsize=12)

plt.ylabel("Features", fontsize=12)

plt.title(
    "Feature Importance - Final Random Forest Model",
    fontsize=15,
    fontweight="bold"
)

# Display values

for bar in bars:

    width = bar.get_width()

    plt.text(

        width + 0.003,

        bar.get_y() + bar.get_height()/2,

        f"{width:.3f}",

        va="center",

        fontsize=9

    )

plt.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(

    r"C:\Users\jayam\Downloads\final_feature_importance.png",

    dpi=600,

    bbox_inches="tight"

)

plt.show()

print("\nFeature Importance Plot Generated Successfully.")
# ==========================================================
# AQIVision Project
# Script: 14_Final_Actual_vs_Predicted.py
#
# Objective:
# Generate the Actual vs Predicted Scatter Plot
# for the Final Random Forest Model.
# ==========================================================

import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# ----------------------------------------------------------
# Calculate R²
# ----------------------------------------------------------

r2 = r2_score(y_test, y_pred)

# ----------------------------------------------------------
# Maximum Value
# ----------------------------------------------------------

max_value = max(

    y_test.max(),

    y_pred.max()

)

# ----------------------------------------------------------
# Create Scatter Plot
# ----------------------------------------------------------

plt.figure(figsize=(8,8))

plt.scatter(

    y_test,

    y_pred,

    s=30,

    alpha=0.65,

    edgecolors="black",

    linewidth=0.3

)

# Perfect Prediction Line

plt.plot(

    [0, max_value],

    [0, max_value],

    'r--',

    linewidth=2.5,

    label="Perfect Prediction"

)

plt.xlim(0, max_value)

plt.ylim(0, max_value)

plt.xlabel(

    "Actual PM$_{2.5}$ ($\\mu g/m^3$)",

    fontsize=12

)

plt.ylabel(

    "Predicted PM$_{2.5}$ ($\\mu g/m^3$)",

    fontsize=12

)

plt.title(

    "Actual vs Predicted PM$_{2.5}$ Concentrations",

    fontsize=15,

    fontweight="bold"

)

# Display R²

plt.text(

    0.05,

    0.95,

    f"$R^2$ = {r2:.3f}",

    transform=plt.gca().transAxes,

    fontsize=12,

    verticalalignment="top",

    bbox=dict(

        facecolor="white",

        edgecolor="black"

    )

)

plt.grid(True, linestyle="--", alpha=0.3)

plt.legend()

plt.tight_layout()

plt.savefig(

    r"C:\Users\jayam\Downloads\final_actual_vs_predicted.png",

    dpi=600,

    bbox_inches="tight"

)

plt.show()

print("\nActual vs Predicted Plot Generated Successfully.")
