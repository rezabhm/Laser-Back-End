import requests
import json


json_request = {

    'reserve': '914705616957727246778695585709597224'

}


src = 'http://backend.lianalaser.com/Reserve/'

r = requests.post(src + 'reserve/information/', json=json_request, headers={'Authorization':'barear 1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
