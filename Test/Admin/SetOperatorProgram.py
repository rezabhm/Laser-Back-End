import requests
import json


json_request = {

    'token': '2',
    'operator_program_list': [

        {

            'date': "1401/11/3",          # ==> show date of program                        $ example : '1401/1101'
            'operator': "Ho3ein",      # ==> operator's username                         $ example : 'Reza'
            'program_turn': "m", # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "Ho3ein", # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/3",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Rza",  # ==> operator's username                         $ example : 'Reza'
            'program_turn': "a",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "reza bhm",  # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/4",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Ho3ein",      # ==> operator's username                         $ example : 'Reza'
            'program_turn': "m",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "Ho3ein",  # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/14",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Reza",  # ==> operator's username                         $ example : 'Reza'
            'program_turn': "a",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "reza bhm",  # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/14",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Reza",  # ==> operator's username                         $ example : 'Reza'
            'program_turn': "m",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "reza bhm",  # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/24",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Ho3ein",      # ==> operator's username                         $ example : 'Reza'
            'program_turn': "a",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "Ho3ein",  # ==> operator operator name                      $ example : 'reza'

        },

        {

            'date': "1401/11/26",  # ==> show date of program                        $ example : '1401/1101'
            'operator': "Ho3ein",      # ==> operator's username                         $ example : 'Reza'
            'program_turn': "a",  # ==> define program is on morning or afternoon   $ example : 'm'
            'operator_name': "Ho3ein",  # ==> operator operator name                      $ example : 'reza'

        },


    ]
}


src = 'http://127.0.0.1:8000/Admin/'

r = requests.post(src + 'set/operator/program/', json=json_request, headers={'token': '1'})

res_data = r.json()
pretty_json = json.dumps(res_data, indent=4)

print('\nStatus Code : ', r.status_code)
print('\n\nResponse JSON : \n\n', pretty_json)
