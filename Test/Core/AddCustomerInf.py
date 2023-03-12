import requests
import json


json_request = {

    'name': 'ahmd',
    'last_name': 'rzb',
    'phone_number': '09124418094',
    'national_code': '4209124418094',
    'house_number': '4209124418094',
    'address': '-',
    'drug_hist': False,
    'decease_hist': False,
    'doctor': '-',

}


src = 'http://127.0.0.1:8000/Core/'

r = requests.post(src + 'add/customer/information/', json=json_request, headers={'Token': '23'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
