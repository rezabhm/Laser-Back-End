import requests
import json


json_request = {

    'token': '2',
    'username': 'arash21',
    'name': 'ahmad',
    'last_name': 'rmz',
    'password': '12345',
    'phone_number': '12345',
    'national_code': '4963214578',
    'address': 'znj',
    'house_number': '3347582695',
    'drug_hist': True,
    'decease_hist': False,
    'doctor': 'Sosan',
    'user_type': 'c',

}


src = 'http://127.0.0.1:8000/Core/'

r = requests.post(src + 'signup/admin/', json=json_request)

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
