import requests
import json


json_request = {

    'reserve': '232'

}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'reserve/information/', json=json_request, headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
