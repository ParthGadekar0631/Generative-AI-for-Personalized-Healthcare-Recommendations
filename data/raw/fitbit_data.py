import os
import requests
from datetime import datetime

# Set your credentials and API endpoint
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BZUkMiLCJzdWIiOiJDQ0Y3S1ciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJzZXQgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNzMyNjE5MDcxLCJpYXQiOjE3MzI1OTAyNzF9.dhnX1EIiE4DoVpnLSUwKNvFWgM6iU2tkifN9QDQaRVY"

today_date = datetime.now().strftime("%Y-%m-%d")

API_ENDPOINT = f"https://api.fitbit.com/1/user/-/activities/date/{today_date}.json"

# Make the API call
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
response = requests.get(API_ENDPOINT, headers=headers)

# Parse the response
data = response.json()

if 'summary' in data:
    summary = data['summary']
    steps = summary.get('steps', 0)
    calories = summary.get('caloriesOut', 0)
    activity_minutes = summary.get('lightlyActiveMinutes', 0)
    
    # Ensure the directory exists
    output_path = "data/raw/fitbit_data.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save data to a CSV file
    with open(output_path, "w") as file:
        file.write("Steps,Calories,ActivityMinutes\n")
        file.write(f"{steps},{calories},{activity_minutes}\n")
    print(f"Activity Data saved to {output_path}")
else:
    print(f"Error fetching activity data: {data}")
