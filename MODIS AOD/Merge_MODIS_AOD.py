# ==========================================================
# AQIVision Project
# Script: 09_Merge_MODIS_AOD.py
#
# Objective:
# Merge the monthly CPCB PM dataset with the monthly
# MODIS MAIAC AOD dataset using City and Month.
#
# Output:
# AQIVision_PM_AOD_Merged.xlsx
# ==========================================================

import pandas as pd

print("=" * 60)
print("AQIVision - Monthly PM + MODIS AOD Integration")
print("=" * 60)

# ----------------------------------------------------------
# Load Monthly PM Dataset
# ----------------------------------------------------------

pm_file = r"C:\Users\jayam\OneDrive\Desktop\AQI\AQI_Excel sheets\monthly_pm.xlsx"

monthly_pm = pd.read_excel(pm_file)

print("\nMonthly PM Dataset Loaded Successfully")
print("Shape :", monthly_pm.shape)

# ----------------------------------------------------------
# Load MODIS MAIAC AOD Dataset
# ----------------------------------------------------------

aod_file = r"C:/Users/jayam/OneDrive/Desktop/AQI/AQI_Excel sheets/AQIVision_Monthly_AOD_2015_2020.csv"

aod = pd.read_csv(aod_file)

print("\nMODIS AOD Dataset Loaded Successfully")
print("Shape :", aod.shape)

# ----------------------------------------------------------
# Ensure Matching Data Types
# ----------------------------------------------------------

monthly_pm["Month"] = monthly_pm["Month"].astype(str)
aod["Month"] = aod["Month"].astype(str)

# ----------------------------------------------------------
# Merge Datasets
# ----------------------------------------------------------

pm_aod = pd.merge(
    monthly_pm,
    aod,
    on=["City", "Month"],
    how="left"
)

# ----------------------------------------------------------
# Remove Unnecessary Earth Engine Columns
# ----------------------------------------------------------

pm_aod = pm_aod.drop(
    columns=["system:index", ".geo"],
    errors="ignore"
)

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nMerged Dataset Shape")
print(pm_aod.shape)

print("\nMissing AOD Values")
print(pm_aod["AOD_550"].isnull().sum())

print("\nFirst Five Records")
print(pm_aod.head())

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

output_file = r"C:\Users\jayam\Downloads\AQIVision_PM_AOD_Merged.xlsx"

pm_aod.to_excel(
    output_file,
    index=False
)

print("\nMerged dataset saved successfully.")

print("\nOutput File:")
print(output_file)

print("\nMODIS MAIAC AOD Integration Completed Successfully.")