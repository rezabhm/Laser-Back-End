import requests
import json


json_request = {

    'username': '23123213213'


}


src = 'http://127.0.0.1:8000/Core/'

r = requests.post(src + 'delete/user/', json=json_request, headers={'Authorization':'barear 1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
