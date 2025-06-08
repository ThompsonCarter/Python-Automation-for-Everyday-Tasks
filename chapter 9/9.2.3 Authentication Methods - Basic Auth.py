from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth(user, pwd)
response = requests.get(url, auth=auth)