import requests
import json

token = '1'

src = 'http://127.0.0.1:8000/Admin/'

r = requests.get(src + 'operator/program/list/1401/3/1', headers={'token': '1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
