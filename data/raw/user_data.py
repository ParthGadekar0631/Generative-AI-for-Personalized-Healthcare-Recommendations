import pandas as pd

# Generate synthetic user data
data = {
    'user_id': [1, 2, 3],
    'age': [25, 30, 35],
    'gender': ['M', 'F', 'M'],
    'medical_history': ['None', 'Hypertension', 'Diabetes'],
    'preferred_workout': ['Cardio', 'Strength', 'Yoga'],
    'steps_per_day': [8000, 5000, 9000],
    'heart_rate': [72, 78, 80],
    'sleep_hours': [7.5, 6.0, 8.0]
}

df = pd.DataFrame(data)
df.to_csv('data/raw/user_data.csv', index=False)