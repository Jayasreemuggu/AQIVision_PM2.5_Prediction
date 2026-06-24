
# ==========================================================
# AQIVision Project
# Section 4: Initial Random Forest Model
# Description:
# 4.1 Model Development
# 4.2 Model Performance
# 4.3 Feature Importance Analysis
# 4.4 Actual vs Predicted Plot
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_excel("city_day_with_coordinates.xlsx")

# Remove rows with missing PM2.5
df = df.dropna(subset=['PM2.5'])

# Date features
df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Encode city
le = LabelEncoder()
df['City_Encoded'] = le.fit_transform(df['City'])

# Fill missing values
pollution_cols = [
    'PM10', 'NO', 'NO2', 'NOx',
    'NH3', 'CO', 'SO2', 'O3'
]

for col in pollution_cols:
    df[col] = df[col].fillna(df[col].median())

# Features
X = df[
    [
        'City_Encoded',
        'Year',
        'Month',
        'Day',
        'PM10',
        'NO',
        'NO2',
        'NOx',
        'NH3',
        'CO',
        'SO2',
        'O3'
    ]
]

# Target
y = df['PM2.5']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

# Random Forest
rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nResults")
print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²  :", round(r2, 3))

#------------------
#Feature Importance
#------------------

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by='Importance',
    ascending=False
)

print(importance_df)

# Plot
plt.figure(figsize=(10,6))
plt.barh(
    importance_df['Feature'],
    importance_df['Importance']
)

plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance - Random Forest')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()


#-------------------------------
#Actual vs Predicted Scatter Plot 
#-------------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.5
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel('Actual PM2.5')
plt.ylabel('Predicted PM2.5')
plt.title('Actual vs Predicted PM2.5 (Improved Random Forest)')

plt.grid(True)
plt.show()

