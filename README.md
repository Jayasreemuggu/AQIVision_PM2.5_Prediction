# AQIVision: PM2.5 Estimation Using Multi-Source Data Fusion Through Machine Learning

## Overview

AQIVision is a machine learning-based framework developed to estimate monthly **PM2.5** concentrations across major Indian cities by integrating heterogeneous environmental datasets. The project combines ground-based air quality observations, satellite-derived aerosol measurements, and meteorological data to improve prediction accuracy through multi-source data fusion.

This project demonstrates the complete machine learning workflow, including data collection, preprocessing, feature engineering, satellite data extraction, meteorological data integration, model development, evaluation, and interpretation.

---

## Project Objectives

* Develop a machine learning model for PM2.5 estimation.
* Integrate multiple environmental datasets into a unified framework.
* Improve prediction accuracy using satellite and meteorological information.
* Analyze the influence of environmental variables on air quality.

---

## Data Sources

### CPCB (Central Pollution Control Board)

* Ground-based air quality measurements
* PM2.5, PM10, NO, NO₂, NOx, NH₃, CO, SO₂, O₃

### MODIS MAIAC (NASA)

* Aerosol Optical Depth (AOD550)
* Extracted using Google Earth Engine

### NASA MERRA-2

Meteorological variables:

* Air Temperature (T2M)
* Specific Humidity (QV2M)
* Surface Pressure (PS)
* Planetary Boundary Layer Height (PBLTOP)
* Wind Components (U10M, V10M)

---

## Methodology

1. Data collection from CPCB
2. Data cleaning and preprocessing
3. Feature engineering
4. Missing value treatment using median imputation
5. MODIS MAIAC AOD extraction using Google Earth Engine
6. MERRA-2 meteorological data extraction
7. Multi-source dataset integration
8. Random Forest Regression model development
9. Model evaluation and feature importance analysis

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Google Earth Engine
* Random Forest Regression
* Matplotlib
* Jupyter Notebook

---

## Model Performance

| Metric   |     Value |
| -------- | --------: |
| R² Score |  **0.82** |
| MAE      | **13.32** |
| RMSE     | **20.53** |

The integration of satellite-derived Aerosol Optical Depth and meteorological variables significantly improved the predictive performance of the model compared to the baseline approach.

---

## Key Features

* Multi-source environmental data fusion
* Satellite remote sensing integration
* Google Earth Engine workflow
* Feature engineering and preprocessing
* Random Forest regression
* Feature importance analysis
* Cross-validation
* Environmental data visualization

---

## Project Workflow

```
CPCB Air Quality Data
          │
          ▼
Data Cleaning & Preprocessing
          │
          ▼
Feature Engineering
          │
          ▼
Google Earth Engine
   ├── MODIS MAIAC AOD
   └── NASA MERRA-2
          │
          ▼
Multi-Source Data Fusion
          │
          ▼
Random Forest Regression
          │
          ▼
Model Evaluation
          │
          ▼
PM2.5 Estimation
```

---

## Repository Structure

```
AQIVision/
│── Data/
│── Notebooks/
│── Scripts/
│── Models/
│── Results/
│── Figures/
│── Report/
└── README.md
```

---

## Author

**Muggu Jaya Sree**

B.Tech, Metallurgical Engineering and Materials Science

Indian Institute of Technology Indore

GitHub: https://github.com/<your-username>

LinkedIn: https://linkedin.com/in/<your-profile>

---

## Future Work

* XGBoost and LightGBM model comparison
* Deep learning approaches for PM2.5 estimation
* Real-time prediction pipeline
* Web-based visualization dashboard
* Integration of additional satellite datasets
* Explainable AI (SHAP/LIME) for model interpretation

---

## License

This project is intended for academic and research purposes.
