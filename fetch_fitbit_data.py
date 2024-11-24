import requests

# Fitbit API details (replace placeholders with actual values)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
ACCESS_TOKEN = "your_access_token"

# API Endpoint for user activity
url = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json"

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Fetch data from Fitbit
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API Data:", response.json())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
