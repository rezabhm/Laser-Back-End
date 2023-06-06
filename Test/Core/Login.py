import requests
import json


json_request = {

    'username': 'reza',
    'password': '1234',

}


src = 'http://127.0.0.1:8000/Core/'

r = requests.post('https://backend.lianalaser.com/Core/login/', json=json_request, timeout=1000000)

print(r)
print(r.headers)

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
