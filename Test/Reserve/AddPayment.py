import requests
import json


json_request = {

    'reserve':'1',
    'off-code':'qwe',
    "laser_area_options": [
        {
            "value": "1",
            "label": "fullbody",
            "operate_time": 5,
            "price": 25000.0,
            "isSelected": True
        },
        {
            "value": "2",
            "label": "kon",
            "operate_time": 5,
            "price": 50000.0,
            "isSelected": True
        },
        {
            "value": "3",
            "label": "kos",
            "operate_time": 5,
            "price": 145000.0,
            "isSelected": True
        },
        {
            "value": "4",
            "label": "mame",
            "operate_time": 5,
            "price": 10000.0,
            "isSelected": False
        }
    ],

    'payment_list': [

        {'price':100000, 'payment_type':'ca'},
        {'price': 50000, 'payment_type': 'cr'},

    ]


}


src = 'http://127.0.0.1:8000/Reserve/'

r = requests.post(src + 'reserve/add/payment/', json=json_request, headers={'Authorization':'Barear d7e2d7da12f34f4491357de77304d68e'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
