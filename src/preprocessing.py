import pandas as pd
import os

# Define file paths
RAW_DATA_PATH = r"C:\Users\parth\Desktop\Projects\Generative-AI-for-Personalized-Healthcare-Recommendations\data\raw\user_data.csv"
PROCESSED_DATA_PATH = r"C:\Users\parth\Desktop\Projects\Generative-AI-for-Personalized-Healthcare-Recommendations\data\processed\fitbit_data_processed.csv"

# Ensure output directory exists
os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

def preprocess_fitbit_data():
    # Load the raw data
    try:
        raw_data = pd.read_csv(RAW_DATA_PATH)
        print(f"Loaded raw data from {RAW_DATA_PATH}")
    except FileNotFoundError:
        print(f"Error: Raw data file not found at {RAW_DATA_PATH}.")
        return

    # Print column names for verification
    print("Columns in raw data:", raw_data.columns.tolist())

    # Handle missing values
    raw_data.fillna(0, inplace=True)

    # Feature engineering
    # Steps-to-Sleep Ratio
    raw_data["StepsToSleepRatio"] = raw_data["steps_per_day"] / (raw_data["sleep_hours"] + 1)

    # Heart Rate Normalized by Age (ensure no division by zero)
    raw_data["HeartRateByAge"] = raw_data["heart_rate"] / (raw_data["age"].replace(0, 1))  # Replace age=0 with 1 to avoid division error

    # Save the processed data
    raw_data.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    preprocess_fitbit_data()
