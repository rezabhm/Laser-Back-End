import requests
import json

token = '9b897f2c5e5344ea87b9bb55e51a59d7'

src = 'http://127.0.0.1:8000/Setting/'

r = requests.get(src + f'list/token={token}/')

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
