import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os

# Define file path
PROCESSED_DATA_PATH = r"C:\Users\parth\Desktop\Projects\Generative-AI-for-Personalized-Healthcare-Recommendations\data\processed\fitbit_data_processed.csv"

def load_data():
    try:
        data = pd.read_csv(PROCESSED_DATA_PATH)
        print("Processed data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: Processed data file not found at {PROCESSED_DATA_PATH}.")
        return None
def prepare_data(data):
    # Define features (X) and labels (y)
    X = data[["steps_per_day", "heart_rate", "sleep_hours"]]  # Example features
    y = data["preferred_workout"]  # Target column
    
    # Encode the target column (convert text to numbers)
    y = y.astype("category").cat.codes
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training completed.")
    return model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    print("\n--- Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
if __name__ == "__main__":
    # Load the data
    data = load_data()

    if data is not None:
        # Prepare data
        X_train, X_test, y_train, y_test = prepare_data(data)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        # Evaluate the model
        evaluate_model(model, X_test, y_test)
