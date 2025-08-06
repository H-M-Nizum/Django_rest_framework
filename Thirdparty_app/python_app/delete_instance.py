import requests
import json

URL = 'http://127.0.0.1:8000/app/create/'

data = {
    'id' : 8,
    
}

# convert python dic to json data
json_data = json.dumps(data)

# create model instance in school model
r = requests.delete(url=URL, data=json_data)
print(r.json())