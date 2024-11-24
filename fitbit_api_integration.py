import requests
from requests.auth import HTTPBasicAuth

# Fitbit API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost/callback"  # Example callback URL
ACCESS_TOKEN = None  # Update after obtaining via OAuth2

# Step 1: Get Authorization Code
def get_authorization_code():
    print("Visit the following URL to authorize:")
    print(f"https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=activity%20heartrate%20sleep")
    code = input("Enter the authorization code from the URL: ")
    return code

# Step 2: Exchange Authorization Code for Access Token
def fetch_access_token(auth_code):
    url = "https://api.fitbit.com/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": CLIENT_ID,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": auth_code
    }
    response = requests.post(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), data=data, headers=headers)
    if response.status_code == 200:
        print("Access Token obtained!")
        return response.json()["access_token"]
    else:
        print("Failed to fetch Access Token.")
        return None

# Step 3: Fetch User Data
def fetch_user_data(token):
    url = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("User Data:", response.json())
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

# Execute the script
if __name__ == "__main__":
    if not ACCESS_TOKEN:
        auth_code = get_authorization_code()
        ACCESS_TOKEN = fetch_access_token(auth_code)
    if ACCESS_TOKEN:
        fetch_user_data(ACCESS_TOKEN)
