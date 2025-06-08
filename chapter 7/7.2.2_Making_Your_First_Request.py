
import requests

url = "https://example.com"
response = requests.get(url)
print("Status:", response.status_code)
print("Preview:", response.text[:200])
