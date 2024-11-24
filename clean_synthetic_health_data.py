import pandas as pd

# Load synthetic data
file_name = "synthetic_health_data.csv"  # Name of the file from the synthetic data generation step
data = pd.read_csv('aw_fb_data.csv')

print("Original Data Shape:", data.shape)

# Cleaning Steps
# 1. Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# 2. Drop rows with missing values (if any)
data_cleaned = data.dropna()

# 3. Validate age range
data_cleaned = data_cleaned[(data_cleaned["age"] >= 18) & (data_cleaned["age"] <= 80)]

# 4. Remove duplicates
data_cleaned = data_cleaned.drop_duplicates()

# 5. Save the cleaned dataset
cleaned_file_name = "cleaned_health_data.csv"
data_cleaned.to_csv(cleaned_file_name, index=False)

print("Cleaned Data Shape:", data_cleaned.shape)
print(f"Cleaned dataset saved as '{cleaned_file_name}'.")
