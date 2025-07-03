import pandas as pd
import random

# Define categories
brands = ["Apple", "Samsung", "Xiaomi", "Google", "OnePlus", "Motorola"]
models = {
    "Apple": ["iPhone 14", "iPhone 15", "iPhone SE"],
    "Samsung": ["Galaxy S24", "Galaxy A54", "Galaxy Z Flip"],
    "Xiaomi": ["Redmi Note 12", "Mi 11 Ultra", "Poco X5"],
    "Google": ["Pixel 7", "Pixel 8", "Pixel 6a"],
    "OnePlus": ["OnePlus 11", "OnePlus Nord", "OnePlus 10T"],
    "Motorola": ["Moto G100", "Moto Edge 30", "Moto G Power"]
}
countries = ["USA", "Germany", "Brazil", "India", "Japan", "UK", "France", "Canada"]
os_types = ["iOS", "Android"]
storage_options = ["64GB", "128GB", "256GB", "512GB"]
ram_options = ["4GB", "6GB", "8GB", "12GB"]
camera_options = ["12MP", "48MP", "50MP", "108MP"]
battery_capacities = ["3000mAh", "4000mAh", "5000mAh"]
release_years = [2022, 2023, 2024]

# Function to classify gamma type
def classify_gamma(price, ram, camera):
    if price > 800 and ram in ["8GB", "12GB"] and camera in ["50MP", "108MP"]:
        return "High"
    elif price > 400 and price <= 800:
        return "Mid"
    else:
        return "Low"

# Generate dataset
data = []
for _ in range(10000):
    brand = random.choice(brands)
    model = random.choice(models[brand])
    price = random.randint(200, 1500)
    country = random.choice(countries)
    os = "iOS" if brand == "Apple" else "Android"
    storage = random.choice(storage_options)
    ram = random.choice(ram_options)
    camera = random.choice(camera_options)
    battery = random.choice(battery_capacities)
    release_year = random.choice(release_years)
    gamma_type = classify_gamma(price, ram, camera)

    data.append([model, brand, price, country, os, storage, ram, camera, battery, release_year, gamma_type])

# Create DataFrame
df = pd.DataFrame(data, columns=["Model", "Brand", "Price (USD)", "Country", "Operating System",
                                 "Storage Capacity", "RAM", "Camera Specs", "Battery Capacity",
                                 "Release Year", "Gamma Type"])

# Save to CSV
df.to_csv("smartphone_sales_data.csv", index=False)

print("Dataset created successfully! File saved as 'smartphone_sales_data.csv'")