from django.http import JsonResponse
from rest_framework.views import APIView

from LIB import utils
from LIB import authentication
from LIB import admin

from . import models
from . import serializer

# Create your views here.


class OperatorProgram(APIView):

    def get(self, request, *args, **kwargs):

        return JsonResponse({'status_code': 400, 'operator_program': "you cant access to this api without valid token"},
                            status=400)

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(json_data['token'])

        if token_status == 201:
            date = json_data['date']
            date_int = utils.cvt_solar_date2ad_int(date)

            # get list of operator program
            operator_list = admin.operator_program_list(date_int)

            # serialize query to json format
            operator_list_serializer = serializer.OperatorProgramSerializer(data=operator_list, many=True)
            status = operator_list_serializer.is_valid()

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,
                'serializer_status': status,
                'operator_program': operator_list_serializer.data,


            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)
