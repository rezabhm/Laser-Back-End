import requests
import json


src = 'http://127.0.0.1:8000/Reserve/'

json_data={

    'reserve':'189501324783785921486111599560986776109'

}

reserve_id = '189501324783785921486111599560986776109'

r = requests.post(src + f'time/list/', json= json_data, headers={

    'Token': '1'

})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
