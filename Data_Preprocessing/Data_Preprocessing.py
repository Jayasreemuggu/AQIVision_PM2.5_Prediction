# ==========================================================
# AQIVision Project
# Section 3: Data Preprocessing
# Description:
#  Feature Engineering
#  Label Encoding
#  Missing Value Analysis
#  Missing Value Visualization
#  Median Imputation
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

file_path = r"C:\Users\jayam\OneDrive\Desktop\AQI\city_day_cleaned.xlsx"

df = pd.read_excel(file_path)

print("=" * 60)
print("AQIVision - Data Preprocessing")
print("=" * 60)


# ==========================================================
# 6. FEATURE ENGINEERING
# ==========================================================

print("\nFEATURE ENGINEERING")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract Year, Month and Day
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print("\nNew Features Created Successfully")

print(df[["Date", "Year", "Month", "Day"]].head())


# ==========================================================
# 7. LABEL ENCODING
# ==========================================================

print("\nLABEL ENCODING")

encoder = LabelEncoder()

df["City_Encoded"] = encoder.fit_transform(df["City"])

print("\nCity Encoding Completed Successfully")

print(df[["City", "City_Encoded"]].head())


# ==========================================================
# 8. MISSING VALUE ANALYSIS
# ==========================================================

print("\nMISSING VALUE ANALYSIS")

pollution_cols = [
    'PM10',
    'NO',
    'NO2',
    'NOx',
    'NH3',
    'CO',
    'SO2',
    'O3'
]

missing_values = df[pollution_cols].isnull().sum()

missing_percentage = (
    missing_values / len(df)
) * 100

print("\nMissing Values")

print(missing_values)

print("\nMissing Percentage (%)")

print(missing_percentage)


# ==========================================================
# 9. MISSING VALUE VISUALIZATION
# ==========================================================

print("\nGENERATING MISSING VALUE PLOT")

plt.figure(figsize=(10,6))

bars = plt.bar(
    missing_values.index,
    missing_values.values,
    edgecolor='black'
)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+80,
        int(bar.get_height()),
        ha='center',
        fontsize=9
    )

plt.title(
    "Distribution of Missing Values Across Pollutant Variables",
    fontsize=15
)

plt.xlabel("Pollutant Variables")
plt.ylabel("Number of Missing Values")

plt.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()

plt.savefig(
    r"C:\Users\jayam\OneDrive\Desktop\AQI\missing_values.png",
    dpi=600
)

plt.show()


# ==========================================================
# 10. MEDIAN IMPUTATION
# ==========================================================

print("\nMEDIAN IMPUTATION")

for col in pollution_cols:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing Values After Imputation")

print(df[pollution_cols].isnull().sum())


# ==========================================================
# SAVE PREPROCESSED DATASET
# ==========================================================

output_file = r"C:\Users\jayam\OneDrive\Desktop\AQI\city_day_preprocessed.xlsx"

df.to_excel(output_file, index=False)

print("\nPreprocessed dataset saved successfully.")

print(f"\nLocation:\n{output_file}")

print("\nData Preprocessing Completed Successfully.")
