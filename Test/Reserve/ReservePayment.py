import requests
import json

reserve = '1'

src = 'http://127.0.0.1:8000/Reserve/'

r = requests.get(src + f'reserve/payment/{reserve}/', headers={'Authorization':'barear d7e2d7da12f34f4491357de77304d68e'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
