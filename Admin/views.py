from django.http import JsonResponse
from rest_framework.views import APIView

from LIB import utils
from LIB import authentication
from LIB import admin

from . import models
from . import serializer

# Create your views here.


class OperatorProgramList(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(json_data, ['token', 'date'])
        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(token=json_data['token'], access_user_type=['a'])

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


class SetOperatorProgram(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(json_data, ['token', 'operator_program_list'])
        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(token=json_data['token'], access_user_type=['a'])

        if token_status == 201:

            # get list of operator program from request's json
            # this param is list of operator program
            # every element is dict and have program's information
            op_list = json_data['operator_program_list']
            result = []

            for op in op_list:

                # op is Dict with above format
                # op = {
                #
                #     date: "string"          ==> show date of program                        $ example : '1401/1101'
                #     operator: "string"      ==> operator's username                         $ example : 'Reza'
                #     program_type : "string" ==> define program is on morning or afternoon   $ example : 'm'
                #     operator_name: "String" ==> operator operator name                      $ example : 'reza'
                #
                # }

                # we must check this program exist or not
                op_model, cp_status = admin.check_program(op)

                # make change
                op = admin.uc_program(op, op_model, cp_status)

                # add result
                result.append(op)

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,
                'operator_program_result': result,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)

