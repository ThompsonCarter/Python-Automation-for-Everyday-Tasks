import requests

endpoint = f"{BASE_URL}/items"
resp = requests.get(endpoint, headers=headers)
resp.raise_for_status()
data = resp.json()
print(type(data), "keys:", data.keys())