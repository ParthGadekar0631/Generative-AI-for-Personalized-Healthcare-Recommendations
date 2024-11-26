import requests

# Replace these with your app's credentials
CLIENT_ID = "23PYRC"
CLIENT_SECRET = "8dea1eaf6da1737a96aaa2513b868047"
REDIRECT_URI = "http://localhost:8080/callback"
AUTHORIZATION_CODE = "b9144f2d8d185b1120d5cfa3f57d38914404003e"  # Replace with the code from Step 2

# Fitbit Token Endpoint
TOKEN_URL = "https://api.fitbit.com/oauth2/token"

# Request headers and data
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "client_id": CLIENT_ID,
    "grant_type": "authorization_code",
    "redirect_uri": REDIRECT_URI,
    "code": AUTHORIZATION_CODE,
}

# Use Basic Authentication (Client ID + Client Secret)
auth = (CLIENT_ID, CLIENT_SECRET)

# Send POST request
response = requests.post(TOKEN_URL, headers=headers, data=data, auth=auth)

# Check response
if response.status_code == 200:
    token_data = response.json()
    print("Access Token:", token_data["access_token"])
    print("Refresh Token:", token_data["refresh_token"])
else:
    print("Error exchanging code for token:", response.json())
