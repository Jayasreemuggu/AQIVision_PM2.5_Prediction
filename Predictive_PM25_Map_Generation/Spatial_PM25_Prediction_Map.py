# ==========================================================
# AQIVision Project
# Script 18
# Spatial Distribution of Average Predicted PM2.5
# ==========================================================

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

print("=" * 60)
print("AQIVision - Spatial Prediction Map")
print("=" * 60)

# ----------------------------------------------------------
# Load Prediction Dataset
# ----------------------------------------------------------

df = pd.read_excel(
    r"C:\Users\jayam\Downloads\Predictive_PM25_Map_Generation\AQIVision_Final_Dataset_With_Coordinates.xlsx")

print("\nPrediction Dataset Loaded")
print("Shape :", df.shape)

# ----------------------------------------------------------
# Average Prediction for Each City
# ----------------------------------------------------------

city_pm = (
    df.groupby(
        ["City", "Latitude", "Longitude"],
        as_index=False
    )["Predicted_PM25"].mean()
)

print("\nCities :", len(city_pm))

# ----------------------------------------------------------
# Create GeoDataFrame
# ----------------------------------------------------------

gdf = gpd.GeoDataFrame(
    city_pm,
    geometry=gpd.points_from_xy(
        city_pm["Longitude"],
        city_pm["Latitude"]
    ),
    crs="EPSG:4326"
)

# ----------------------------------------------------------
# Load India Boundary
# ----------------------------------------------------------

url = "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_admin_0_countries.zip"

world = gpd.read_file(url)

india = world[world["ADMIN"] == "India"]

# ----------------------------------------------------------
# Figure
# ----------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 12))

india.plot(
    ax=ax,
    color="#F7F7F7",
    edgecolor="black",
    linewidth=1.4
)

# ----------------------------------------------------------
# Dynamic Colour Scale
# ----------------------------------------------------------

norm = colors.Normalize(
    vmin=city_pm["Predicted_PM25"].min(),
    vmax=city_pm["Predicted_PM25"].max()
)

gdf.plot(
    ax=ax,
    column="Predicted_PM25",
    cmap="RdYlGn_r",
    norm=norm,
    legend=True,
    markersize=140,
    edgecolor="black",
    linewidth=0.6,
    alpha=0.95
)

# ----------------------------------------------------------
# Colour Bar
# ----------------------------------------------------------

cbar = fig.axes[-1]

cbar.set_ylabel(
    "Average Predicted PM$_{2.5}$ ($\mu g/m^3$)",
    fontsize=11
)

# ----------------------------------------------------------
# Label Offsets
# ----------------------------------------------------------

offsets = {

    "Delhi": (8, 12),
    "Gurugram": (8, -12),
    "Faridabad": (8, 20),

    "Chandigarh": (8, 10),

    "Shillong": (8, -10),

    "Kolkata": (8, -10),

    "Chennai": (8, 10),

    "Mumbai": (8, -10),

    "Ahmedabad": (-30, 10),

    "Lucknow": (8, 10),

    "Patna": (8, 10)

}

# ----------------------------------------------------------
# Labels
# ----------------------------------------------------------

for _, row in gdf.iterrows():

    dx, dy = offsets.get(
        row["City"],
        (6, 6)
    )

    ax.annotate(
        row["City"],
        (row.geometry.x, row.geometry.y),
        xytext=(dx, dy),
        textcoords="offset points",
        fontsize=8,
        fontweight="bold"
    )

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

ax.set_title(
    "Spatial Distribution of Predicted PM$_{2.5}$",
    fontsize=18,
    fontweight="bold"
)

ax.set_xlabel("Longitude", fontsize=12)
ax.set_ylabel("Latitude", fontsize=12)

ax.grid(False)

plt.tight_layout()

# ----------------------------------------------------------
# Save Figure
# ----------------------------------------------------------

plt.savefig(
    r"C:\Users\jayam\Downloads\Average_Predicted_PM25_India_Map.png",
    dpi=800,
    bbox_inches="tight"
)

plt.show()

print("\nMap Saved Successfully.")