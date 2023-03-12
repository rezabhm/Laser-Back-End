import requests
import json


src = 'http://127.0.0.1:8000/Core/'

username = 'reza'

r = requests.get(src + f'login/customer/{username}')

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
