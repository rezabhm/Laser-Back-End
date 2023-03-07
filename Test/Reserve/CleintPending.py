import requests
import json


json_request = {

    'laser_area_list': [

        '299067747061395756237728229629163349237',
        '27764495362301563721785418712887719484',

    ],

}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'client/pending/reserve/', json=json_request, headers={'Token':'9b897f2c5e5344ea87b9bb55e51a59d7'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
