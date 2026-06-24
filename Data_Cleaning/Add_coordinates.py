# ==========================================================
# AQIVision Project
# Merge Latitude and Longitude into Final Dataset
#
# Input:
# 1. AQIVision_Final_Dataset.xlsx
# 2. city_day_with_coordinates.xlsx
#
# Output:
# AQIVision_Final_Dataset_With_Coordinates.xlsx
# ==========================================================

import pandas as pd

print("=" * 60)
print("AQIVision - Merging City Coordinates")
print("=" * 60)

# ----------------------------------------------------------
# Load Final Dataset
# ----------------------------------------------------------

final_dataset = pd.read_excel(
    r"C:\Users\jayam\Downloads\AQIVision_Final_Dataset.xlsx"
)

print("\nFinal Dataset Loaded Successfully")
print("Shape :", final_dataset.shape)

# ----------------------------------------------------------
# Load Coordinate Dataset
# ----------------------------------------------------------

coordinates = pd.read_excel(
    r"C:\Users\jayam\OneDrive\Desktop\AQI\AQI_Excel sheets\city_day_with_coordinates.xlsx")

print("\nCoordinate Dataset Loaded Successfully")
print("Shape :", coordinates.shape)

# ----------------------------------------------------------
# Extract Unique City Coordinates
# ----------------------------------------------------------

coordinates = coordinates[
    ["City", "Latitude", "Longitude"]
].drop_duplicates(subset="City")

print("\nUnique Cities :", len(coordinates))

# ----------------------------------------------------------
# Merge Coordinates
# ----------------------------------------------------------

merged_dataset = pd.merge(
    final_dataset,
    coordinates,
    on="City",
    how="left"
)

# ----------------------------------------------------------
# Check Missing Coordinates
# ----------------------------------------------------------

print("\nMissing Latitude :",
      merged_dataset["Latitude"].isnull().sum())

print("Missing Longitude :",
      merged_dataset["Longitude"].isnull().sum())

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

output_file = (
    r"C:\Users\jayam\Downloads\AQIVision_Final_Dataset_With_Coordinates.xlsx"
)

merged_dataset.to_excel(
    output_file,
    index=False
)

print("\nDataset Saved Successfully")
print(output_file)

print("\nFinal Dataset Shape")
print(merged_dataset.shape)

print("\nFirst Five Rows")
print(merged_dataset.head())

print("\nCoordinate Merge Completed Successfully.")
