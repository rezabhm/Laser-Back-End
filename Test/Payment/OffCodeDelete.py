import requests
import json


json_request = {

    'token': '1',
    'off_code': 'Asd1',

}


src = 'http://127.0.0.1:8000/Payment/'

r = requests.post(src + 'off/code/delete/', json=json_request)

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
