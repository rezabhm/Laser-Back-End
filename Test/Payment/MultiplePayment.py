import requests
import json


json_request = {

    'reserve': '21',
    'payment_list': [

        {
            'price': 20000,
            'payment_type': 'ca'
        },

        {
            'price': 1000,
            'payment_type': 'cr'
        },

        {
            'price': 30000,
            'payment_type': 'ch'
        },

    ],

}


src = 'http://127.0.0.1:8000/Payment/'

r = requests.post(src + 'multiple/payment/', json=json_request, headers={'Token':'1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
