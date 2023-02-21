from django.http import JsonResponse
from rest_framework.views import APIView

from LIB import utils
from LIB import authentication
from LIB import core

from . import models
from . import serializer

# Create your views here.


class SignUpCustomer(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)
        json_data['user_type'] = 'c'

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['token', 'username', 'name', 'last_name', 'password', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=json_data['token'],
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status = core.check_username(json_data['username'], user_type='c', national_code=json_data['national_code'])

            if status:

                return JsonResponse({

                    'status_code': 400,
                    'status': 'user exist ...',

                }, status=400)

            # create user
            core.create_user(json_data)

            return JsonResponse({

                'status_code': 201,
                'status': 'user successfully create ...',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class SignUpAdmin(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['token', 'username', 'name', 'last_name', 'password', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor', 'user_type']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=json_data['token'],
            access_user_type=['a']

        )

        if token_status == 201:

            # check customer user
            status = core.check_username(

                json_data['username'],
                user_type=json_data['user_type'],
                national_code=json_data['national_code']

            )

            if status:

                return JsonResponse({

                    'status_code': 400,
                    'status': 'user exist ...',

                }, status=400)

            # create user
            core.create_user(json_data)

            return JsonResponse({

                'status_code': 201,
                'status': 'user successfully create ...',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class Login(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'password']

        )

        if status:
            return response

        # check customer user
        status, status_txt, token = core.login(

            username=json_data['username'],
            password=json_data['password']

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,
            'token': token,

        }, status=201)


class LogOut(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['token']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=json_data['token'],
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            core.logout(json_data['token'])

            return JsonResponse({

                'status_code': 201,
                'status_text': 'logged out',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ForgotPassword(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response

        # check customer user
        status, status_txt = core.forgot_password(

            username=json_data['username'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=201)


class ProveForgotPassword(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'code']

        )

        if status:
            return response

        # check customer user
        status, status_txt = core.prove_forgot_password(

            username=json_data['username'],
            code=json_data['code'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=201)


class ChangePassword(APIView):

    def get(self, request, *args, **kwargs):

        return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'code', 'password']

        )

        if status:
            return response

        # check customer user
        status, status_txt = core.change_password(

            username=json_data['username'],
            password=json_data['password'],
            code=json_data['code'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=201)