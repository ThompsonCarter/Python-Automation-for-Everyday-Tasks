try:
    resp = requests.get(endpoint, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Network error:", e)