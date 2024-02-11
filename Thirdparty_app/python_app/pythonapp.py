import requests

URL = 'http://127.0.0.1:8000/app/school/'

response = requests.get(url=URL)

json_data = response.json()
print(json_data)