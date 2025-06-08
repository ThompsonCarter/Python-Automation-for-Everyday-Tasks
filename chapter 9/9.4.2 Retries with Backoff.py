from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502,503,504])
session.mount("https://", HTTPAdapter(max_retries=retries))

resp = session.get(endpoint, headers=headers)