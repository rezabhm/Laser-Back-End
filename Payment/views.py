from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, payment

from rest_framework.permissions import AllowAny

from . import models, serializer, swagger_schema


# Create your views here.


class OffCodeList(GenericAPIView):

    """

    لیست کد ها تخفیف

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # list of off code
            off_code_list = models.OffCode.objects.all()

            # serializer
            off_code_serializer = serializer.OffCodeSerializer(data=off_code_list, many=True)
            off_code_serializer.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ...',
                'off_code_list': off_code_serializer.data,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class OffCodeDelete(GenericAPIView):
    """

    حذف کد تخفیف

    """

    serializer_class = swagger_schema.OffCodeDeleteSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['off_code', ]

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = payment.delete_off_code(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class OffCodeCreate(GenericAPIView):
    """

    تولید کد تخفیف

    """

    serializer_class = swagger_schema.OffCodeCreateSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['off_code', 'amount', ]

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = payment.create_off_code(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class OffCodeAddReserve(GenericAPIView):
    """

    اضافه کردن کد تخفیف به رزرو

    """

    serializer_class = swagger_schema.OffCodeAddReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['off_code', 'reserve', ]

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = payment.off_code_add_reserve(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class MultiplePayment(GenericAPIView):
    """

    پرداخت های نوبت

    """

    serializer_class = swagger_schema.OffCodeAddReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['payment_list', 'reserve', ]

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = payment.multiple_payment(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)
