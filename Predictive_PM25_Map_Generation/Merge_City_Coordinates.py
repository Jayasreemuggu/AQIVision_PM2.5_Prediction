# ==========================================================
# AQIVision Project
# Script 16
# Merge City Coordinates with Final Dataset
# ==========================================================

import pandas as pd

print("=" * 60)
print("AQIVision - Merge City Coordinates")
print("=" * 60)

# ----------------------------------------------------------
# Load Final Dataset
# ----------------------------------------------------------

final_df = pd.read_excel(
    r"C:\Users\jayam\OneDrive\Desktop\AQI\AQI_Excel sheets\AQIVision_Final_Dataset.xlsx"
)

print("\nFinal Dataset Loaded Successfully")
print("Shape :", final_df.shape)

# ----------------------------------------------------------
# Load Coordinate Dataset
# ----------------------------------------------------------

coord_df = pd.read_excel(
    r"C:\Users\jayam\OneDrive\Desktop\AQI\AQI_Excel sheets\city_day_with_coordinates.xlsx"
)

print("\nCoordinate Dataset Loaded Successfully")
print("Shape :", coord_df.shape)

# ----------------------------------------------------------
# Keep Unique Coordinates
# ----------------------------------------------------------

coord_df = coord_df[
    ["City", "Latitude", "Longitude"]
].drop_duplicates(subset="City")

print("\nUnique Cities :", len(coord_df))

# ----------------------------------------------------------
# Merge Coordinates
# ----------------------------------------------------------

merged_df = pd.merge(
    final_df,
    coord_df,
    on="City",
    how="left"
)

# ----------------------------------------------------------
# Check Missing Coordinates
# ----------------------------------------------------------

print("\nMissing Latitude  :", merged_df["Latitude"].isnull().sum())
print("Missing Longitude :", merged_df["Longitude"].isnull().sum())

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

output_path = (
    r"C:\Users\jayam\Downloads\AQIVision_Final_Dataset_With_Coordinates.xlsx"
)

merged_df.to_excel(
    output_path,
    index=False
)

print("\nMerged Dataset Saved Successfully")

print(output_path)

print("\nFinal Shape :", merged_df.shape)

print("\nDone.")
