import requests

params = {"who": "everybody"}
r = requests.post("http://localhost:8000/hi", json=params)
print(r.json())