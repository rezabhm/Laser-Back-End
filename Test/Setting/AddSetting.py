import requests
import json


json_request = {

    'morning_time': 12,
    'afternoon_time': 18,
    'trust_price': 12000,

}


src = 'http://127.0.0.1:8000/Setting/'

r = requests.post(src + 'change/setting/', json=json_request, headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
