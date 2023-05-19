import requests
import json


json_request = {

    'from_': '',
    'to': '',

}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'reserve/list/', json=json_request, headers={'Authorization':'barear 4804fa170acc47078f14afc1cf7d4384'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
