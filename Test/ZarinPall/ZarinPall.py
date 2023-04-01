import requests
import json


json_request = {

    'amount': '5000',
    'reserve': '1213',

}


src = 'http://127.0.0.1:8000/zarin/pall/'

r = requests.post(src + 'request/', json_request)

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
