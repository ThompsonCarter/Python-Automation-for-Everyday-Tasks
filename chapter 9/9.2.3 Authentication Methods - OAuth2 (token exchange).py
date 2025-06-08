token_resp = requests.post(
    f"{BASE_URL}/oauth2/token",
    data={"grant_type": "client_credentials"},
    auth=(API_KEY, API_SECRET)
)
token = token_resp.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}