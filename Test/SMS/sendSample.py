import requests


src = 'http://ippanel.com/api/select'

json_request = {

    'op': 'send',
    'uname': '09104734870',
    'pass': '4400080072',
    'message': 'be emad kir kocholo salam bereson',
    'from': '5000125475',
    'to': ['09339192819', ],

}


r = requests.post(src, json=json_request)

print('\nStatus Code : ', r.content)
print('\n\nResponse JSON : \n\n', r.content)
