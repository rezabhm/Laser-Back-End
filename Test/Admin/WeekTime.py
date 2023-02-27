import requests
import json

week = '-1'

src = 'http://127.0.0.1:8000/Admin/'

r = requests.get(src + f'week/time/{week}/')

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
