import requests
import json


json_request = {

    'name': 'کون',
    'price': '850000',
    'operate_time': 25,
    'deadline_reset': 40,

}


src = 'http://127.0.0.1:8000/Laser/'

r = requests.post(src + 'add/new/laser/area/', headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
