import requests
import json



src = 'http://127.0.0.1:8000/Core/'

r = requests.get(src + 'comment/list/', headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
