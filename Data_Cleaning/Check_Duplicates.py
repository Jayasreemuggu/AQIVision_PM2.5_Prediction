import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(r"C:\Users\jayam\OneDrive\Desktop\AQI\city_day_with_coordinates.xlsx")

pollution_cols = [
    'PM10', 'NO', 'NO2', 'NOx',
    'NH3', 'CO', 'SO2', 'O3'
]

print("Missing Values:\n")
print(df[pollution_cols].isnull().sum())

print("\nPercentage Missing:\n")
print((df[pollution_cols].isnull().sum() / len(df)) * 100)

missing = df[pollution_cols].isnull().sum()

plt.figure(figsize=(8,5))
missing.sort_values().plot(kind='bar')
plt.title('Missing Values by Feature')
plt.ylabel('Count')
plt.xlabel('Pollution Features')
plt.grid(axis='y')
plt.show()
