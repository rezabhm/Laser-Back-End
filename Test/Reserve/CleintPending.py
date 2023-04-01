import requests
import json


json_request = {

    'laser_area_list': [

        '299067747061395756237728229629163349237',

    ],

}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'client/pending/reserve/', json=json_request, headers={'Authorization':'barear 1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
