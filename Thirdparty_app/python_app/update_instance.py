import requests
import json

URL = 'http://127.0.0.1:8000/app/create/'

data = {
    'id' : 244,
    'teacher_name' : 'bb123',
    'course_name' : 'www',
    'course_duration' : 3,
    'seat' : 50
    
}

# convert python dic to json data
json_data = json.dumps(data)

# create model instance in school model
r = requests.put(url=URL, data=json_data)
print(r.json())