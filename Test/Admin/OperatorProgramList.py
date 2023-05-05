import requests
import json

token = '1'

src = 'http://backend.lianalaser.com/Admin/'

r = requests.get(src + 'operator/program/list/1402/2/2', headers={'Authorization': 'barear 4804fa170acc47078f14afc1cf7d4384'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
