from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, setting
from rest_framework.permissions import AllowAny

from . import swagger_schema


# Create your views here.


class SettingList(GenericAPIView):

    """

    لیست اطلاعات تنظیمات

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    def get(self, request, token, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=token,
            access_user_type=['a']

        )

        if token_status == 201:

            with open('morning_time.txt') as fd:
                morning_time = fd.read()

            with open('afternoon_time.txt') as fd:
                afternoon_time = fd.read()

            with open('trust_price.txt') as fd:
                trust_price = fd.read()

            data = {

                'trust_price': float(trust_price),
                'afternoon_time': afternoon_time,
                'morning_time': morning_time,

            }

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ...',
                'morning_time': data['morning_time'],
                'afternoon_time': data['afternoon_time'],
                'trust_price': data['trust_price'],

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ChangeSetting(GenericAPIView):
    """

    تفییر اطلاعات تنظیمات

    """

    serializer_class = swagger_schema.AddSetting
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['token', 'morning_time', 'afternoon_time', 'trust_price',]

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=json_data['token'],
            access_user_type=['a']

        )

        if token_status == 201:

            with open('morning_time.txt', 'w') as fd:
                fd.write(str(json_data['morning_time']))

            with open('afternoon_time.txt', 'w') as fd:
                fd.write(str(json_data['afternoon_time']))

            with open('trust_price.txt' , 'w') as fd:
                fd.write(str(json_data['trust_price']))

            return JsonResponse({

                'status_code': 200,
                'status': 'successfully',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)

