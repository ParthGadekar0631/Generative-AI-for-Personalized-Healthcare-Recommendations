import pandas as pd
import json

# Load cleaned synthetic data
synthetic_data_file = "cleaned_health_data.csv"
synthetic_data = pd.read_csv(synthetic_data_file)

# Load Fitbit real-time data (replace with actual Fitbit API data file or response parsing)
fitbit_data = [
    {"user_id": "uuid-1", "steps": 8500, "heart_rate": 72, "sleep_hours": 6.5},
    {"user_id": "uuid-2", "steps": 12000, "heart_rate": 68, "sleep_hours": 7.0},
    # Example entries
]

# Convert Fitbit data to a DataFrame
fitbit_df = pd.DataFrame(fitbit_data)

# Merge datasets on 'user_id' (simulated in this case)
merged_data = pd.merge(synthetic_data, fitbit_df, on="user_id", how="inner")

# Save the merged dataset
merged_file_name = "merged_health_data.csv"
merged_data.to_csv(merged_file_name, index=False)

print("Merged dataset saved as:", merged_file_name)
