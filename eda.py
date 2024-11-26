import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file path for processed data
PROCESSED_DATA_PATH = r"C:\Users\parth\Desktop\Projects\Generative-AI-for-Personalized-Healthcare-Recommendations\data\processed\fitbit_data_processed.csv"

def load_data():
    try:
        data = pd.read_csv(PROCESSED_DATA_PATH)
        print("Processed data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: Processed data file not found at {PROCESSED_DATA_PATH}.")
        return None
def basic_statistics(data):
    print("\n--- Basic Statistics ---")
    print(data.describe())  # Summary statistics

    print("\n--- Missing Values ---")
    print(data.isnull().sum())  # Check for missing values
def plot_distributions(data):
    numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns

    print("\n--- Plotting Distributions ---")
    for column in numeric_columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(data[column], kde=True, bins=30)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()
def correlation_analysis(data):
    print("\n--- Correlation Matrix ---")
    correlation_matrix = data.corr()
    print(correlation_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()
if __name__ == "__main__":
    # Load processed data
    data = load_data()

    if data is not None:
        # Perform EDA
        basic_statistics(data)
        plot_distributions(data)
        correlation_analysis(data)
