import requests
import json


json_request = {

    'token': '2',
    'operator_program_list': [
        {
            "id": "1401/1/1m",
            "date_str": "1401/1/1",
            "program_turn": "m",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/1a",
            "date_str": "1401/1/1",
            "program_turn": "a",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/2m",
            "date_str": "1401/1/2",
            "program_turn": "m",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/2a",
            "date_str": "1401/1/2",
            "program_turn": "a",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/3m",
            "date_str": "1401/1/3",
            "program_turn": "m",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/3a",
            "date_str": "1401/1/3",
            "program_turn": "a",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/4m",
            "date_str": "1401/1/4",
            "program_turn": "m",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/4a",
            "date_str": "1401/1/4",
            "program_turn": "a",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/5m",
            "date_str": "1401/1/5",
            "program_turn": "m",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/5a",
            "date_str": "1401/1/5",
            "program_turn": "a",
            "operator_name": "reza",
            "operator": "reza"
        },
        {
            "id": "1401/1/6m",
            "date_str": "1401/1/6",
            "program_turn": "m",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/6a",
            "date_str": "1401/1/6",
            "program_turn": "a",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/7m",
            "date_str": "1401/1/7",
            "program_turn": "m",
            "operator_name": "",
            "operator": ""
        },
        {
            "id": "1401/1/7a",
            "date_str": "1401/1/7",
            "program_turn": "a",
            "operator_name": "",
            "operator": ""
        }
    ]

}


src = 'http://backend.lianalaser.com/Admin/'

r = requests.post(src + 'set/operator/program/', json=json_request, headers={'Authorization': 'barear 4804fa170acc47078f14afc1cf7d4384'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
print(src + 'set/operator/program/')