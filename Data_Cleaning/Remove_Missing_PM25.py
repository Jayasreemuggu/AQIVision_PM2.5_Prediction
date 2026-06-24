# ==========================================================
# AQIVision Project
# Section 2: Data Cleaning
# Script: 04_Check_Duplicates.py
# Description:
# Checks the cleaned dataset for duplicate records.
# ==========================================================

import pandas as pd

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

file_path = r"C:\Users\jayam\OneDrive\Desktop\AQI\city_day_cleaned.xlsx"


df = pd.read_excel(file_path)

print("=" * 60)
print("AQIVision - Duplicate Record Analysis")
print("=" * 60)

# ----------------------------------------------------------
# Dataset Shape
# ----------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

# ----------------------------------------------------------
# Check Duplicate Records
# ----------------------------------------------------------

duplicate_count = df.duplicated().sum()

print(f"\nNumber of Duplicate Records: {duplicate_count}")

# ----------------------------------------------------------
# Display Duplicate Records (if any)
# ----------------------------------------------------------

if duplicate_count > 0:
    print("\nDuplicate Records:")
    print(df[df.duplicated()])
else:
    print("\nNo duplicate records were found.")

print("\nDuplicate Analysis Completed Successfully.")
