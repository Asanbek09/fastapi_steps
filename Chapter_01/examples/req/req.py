import requests

params = {"who": "everybody"}
r = requests.get("http://localhost:8000/hi", params=params)
r.json()