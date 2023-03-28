import requests
import json


src = 'http://127.0.0.1:8000/Reserve/'
reserve = '91470561695772087246778695585709597224'

r = requests.get(src + f'reserve/time/range/{reserve}', headers={'Authorization':'barear 1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
