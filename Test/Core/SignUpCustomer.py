import requests
import json


json_request = {

    'token': '2',
    'username': 'ahmad234',
    'name': 'ahmad',
    'last_name': 'rmz',
    'password': '12345',
    'phone_number': '12345',
    'national_code': '4125963214578',
    'address': 'znj',
    'house_number': '3347582695',
    'drug_hist': True,
    'decease_hist': False,
    'door': 'sosan',

}


src = 'http://127.0.0.1:8000/Core/'

r = requests.post(src + 'signup/customer/', json=json_request)

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
