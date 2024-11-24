import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker and seed for reproducibility
fake = Faker()
np.random.seed(42)

# Number of records to generate
num_records = 500

# Generate synthetic data
data = {
    "user_id": [fake.uuid4() for _ in range(num_records)],
    "age": np.random.randint(18, 80, size=num_records),
    "gender": np.random.choice(["Male", "Female", "Other"], size=num_records),
    "medical_history": np.random.choice(
        ["None", "Diabetes", "Hypertension", "Asthma", "Heart Disease"], size=num_records
    ),
    "dietary_preferences": np.random.choice(
        ["Vegan", "Vegetarian", "Keto", "Omnivore", "Pescatarian"], size=num_records
    ),
    "activity_level": np.random.choice(
        ["Sedentary", "Moderate", "Active", "Very Active"], size=num_records
    ),
    "average_steps": np.random.randint(1000, 15000, size=num_records),
    "average_heart_rate": np.random.randint(60, 100, size=num_records),
    "sleep_hours": np.random.uniform(4, 10, size=num_records).round(1),
}

# Create DataFrame
synthetic_data = pd.DataFrame(data)

# Save to CSV
synthetic_data.to_csv("synthetic_health_data.csv", index=False)

print("Synthetic data generated and saved as 'synthetic_health_data.csv'.")
