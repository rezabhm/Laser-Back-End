import requests
import json

reserve = '7004527397671361538141393167307103497'

src = 'http://backend.lianalaser.com/Reserve/'

r = requests.get(src + f'reserve/payment/{reserve}/', headers={'Authorization':'barear 4804fa170acc47078f14afc1cf7d4384'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
