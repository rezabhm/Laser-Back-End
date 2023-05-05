import requests
import json

reserve = '140990025231674443400925908216295156995'

src = 'http://127.0.0.1:8000/Reserve/'

r = requests.get(src + f'reserve/payment/{reserve}/', headers={'Authorization':'barear 985094aeb18743c48eaff537f8838e4c'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
