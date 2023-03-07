import requests
import json


json_request = {

    'time_range': '8-10',
    'date': '1401/2/20',

}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'client/add/time/', json=json_request, headers={'Token':'9b897f2c5e5344ea87b9bb55e51a59d7'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
