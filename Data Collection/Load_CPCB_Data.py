# ==========================================================
# AQIVision Project
# Section 1: Data Collection
# Script: 01_Load_CPCB_Data.py
# Description:
# Loads the original CPCB air quality dataset and performs
# a preliminary inspection.
# ==========================================================

# Import required libraries
import pandas as pd

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

dataset_path = "C:/Users/jayam/OneDrive/Desktop/AQI/city_day.csv"

df = pd.read_csv(dataset_path)

print("=" * 60)
print("AQIVision - CPCB Air Quality Dataset")
print("=" * 60)

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nDataset Shape")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

# ----------------------------------------------------------
# Display First Five Records
# ----------------------------------------------------------

print("\nFirst Five Rows")
print(df.head())

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nDataset Information")
print(df.info())

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\nMissing Values in Each Column")
print(df.isnull().sum())

# ----------------------------------------------------------
# Statistical Summary
# ----------------------------------------------------------

print("\nStatistical Summary")
print(df.describe())

print("\nData Collection Completed Successfully.")
