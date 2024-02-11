import requests
import json

URL = 'http://127.0.0.1:8000/app/create/'

data ={
    'teacher_name' : 'dddd',
    'course_name' : 'www',
    'course_duration' : 3,
    'seat' : 50
}

# convert python dic to json data
json_data = json.dumps(data)

# create model instance in school model
send_data = requests.post(url=URL, data=json_data)