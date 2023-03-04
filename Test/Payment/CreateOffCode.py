import requests
import json


json_request = {

    'off_code': 'Asd158',
    'amount': '99',

}


src = 'http://127.0.0.1:8000/Payment/'

r = requests.post(src + 'off/code/create/', json=json_request, headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
