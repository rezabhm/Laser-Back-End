import requests
import json


src = 'http://backend.lianalaser.com/Reserve/'
reserve = '218726306752453915531603505248622526279'

r = requests.get(src + f'reserve/time/range/{reserve}/', headers={'Authorization':'barear 1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
