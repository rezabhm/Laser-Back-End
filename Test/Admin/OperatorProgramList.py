import requests
import json

token = '1'

src = 'http://127.0.0.1:8000/Admin/'

r = requests.get(src + 'operator/program/list/1401/1/1', headers={'Authorization': 'barear 985094aeb18743c48eaff537f8838e4c'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
