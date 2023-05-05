from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, reserve
from rest_framework.permissions import AllowAny

from . import models, serializer, swagger_schema


# Create your views here.


class ReserveList(GenericAPIView):
    """

    گزارش گیری نوبت ها ( در صورت خالی وارد کردن ('') پارامتر های ورودی نوبت های روز را میدهد)

    """

    serializer_class = swagger_schema.ReserveListSerializer
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
            ['from_', 'to']

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
            response_data = reserve.reserve_list(

                json_data

            )

            return JsonResponse({

                'status_code': 200,
                'status': 'successfully',
                'all_list': response_data[0],
                'complete_list': response_data[1],
                'un_complete_list': response_data[2],
                'all_list_length': response_data[3],
                'complete_list_length': response_data[4],
                'un_complete_list_length': response_data[5],
                'total_price': response_data[6],

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class UserReserveList(GenericAPIView):
    """

    لیست نوبت های مراجعین را بر میگرداند

    """

    serializer_class = swagger_schema.NewReserveSerializer
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
            ['username']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            response_data = reserve.user_reserve_list(

                json_data

            )

            return JsonResponse({

                'status_code': 200,
                'status': 'successfully',
                'reserve_list': response_data,
                'last_reserve': response_data[-1] if len(response_data) > 0 else None,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ReserveInformation(GenericAPIView):
    """

    جزعیات نوبت

    """

    serializer_class = swagger_schema.ReserveInformationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, reserve_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text, reserve_data = reserve.reserve_inf(

                {'reserve':reserve_id}

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,
                'reserve': reserve_data[0],
                'payment_list': reserve_data[1],

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ReservePayment(GenericAPIView):
    """

    جزعیات نوبت

    """

    serializer_class = swagger_schema.ReserveInformationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, reserve_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text, reserve_data = reserve.reserve_pay(

                {'reserve':reserve_id}

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,
                'id': reserve_id,
                'name': reserve_data[0],
                'turn_time': reserve_data[1],
                'total_price_amount': reserve_data[2],
                'laser_area_list': reserve_data[3],
                'laser_area_options': reserve_data[4]

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CancelReserve(GenericAPIView):
    """

    کنسل کردن نوبت توسط منشی و مشتری

    """

    serializer_class = swagger_schema.CancelReserveSerializer
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
            ['reserve', 'cancel_type', 'sms_status']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = reserve.cancel_reserve(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,


            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ReserveLaserArea(GenericAPIView):
    """

    لیست نواحی لیزر برای نوبت

    """

    serializer_class = swagger_schema.ReserveInformationSerializer
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
            ['reserve']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text, laser_area_list = reserve.reserve_laser_area(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,
                'laser_area_list': laser_area_list


            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class EditReserveLaserArea(GenericAPIView):
    """

    تغییر تواحی لیزر برای نوبت

    """

    serializer_class = swagger_schema.EditReserveSerializer
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
            ['reserve', 'laser_area_list']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = reserve.edit_reserve_laser_area(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,


            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ReceptionAddReserve(GenericAPIView):
    """

    ثبت نوبت غیر جضوری

    """

    serializer_class = swagger_schema.NewReserveSerializer
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
            ['username']

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
            status_code, status_text, reserve_id = reserve.new_reserve_reception(

                json_data

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,
                'reserve': reserve_id,


            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ProveReserve(GenericAPIView):

    """

    نهایی سازی و تایید نوبت

    """

    serializer_class = swagger_schema.ReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(request, access_user_type=['a'])

        if token_status == 201:

            status, status_text = reserve.prove_reserve(request.headers['Authorization'].split(' ')[-1])

            return JsonResponse({

                'status_code': status,
                'status': status_text,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class TimeList(GenericAPIView):

    """

    لیست زمان های قابل انتخاب نوبت

    """

    serializer_class = swagger_schema.ReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, reserve_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(request, access_user_type=['a'])

        if token_status == 201:

            status, status_text, json_response = reserve.time_list(reserve_id)

            return JsonResponse({

                'status_code': status,
                'status': status_text,
                'time_data': json_response

            }, status=int(status))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ReserveTimeRange(GenericAPIView):

    """

    بازه ی زمانی را برای نوبت میدهد

    """

    serializer_class = swagger_schema.ReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, reserve_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(request, access_user_type=['a'])

        if token_status == 201:

            status, status_text, date, time_range = reserve.reserve_time_range(reserve_id)

            return JsonResponse({

                'status_code': status,
                'status': status_text,
                'date': date,
                'time_range': time_range

            }, status=int(status))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CancelReserveTimeRange(GenericAPIView):

    """

    بازه ی زمانی را برای نوبت کنسل میکند

    """

    serializer_class = swagger_schema.ReserveSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, reserve_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(request, access_user_type=['a'])

        if token_status == 201:

            status, status_text = reserve.cancel_reserve_time_range(reserve_id)

            return JsonResponse({

                'status_code': status,
                'status': status_text,

            }, status=int(status))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ClientPendingReserve(GenericAPIView):
    """

    رزرو اولیه نوبت توسط مشتری
    """

    serializer_class = swagger_schema.PendingReserveSerializer
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
            ['laser_area_list']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text, reserve_id = reserve.client_reserve_pending(

                request.headers['Authorization'].split(' ')[-1],
                json_data['laser_area_list']

            )

            return JsonResponse({

                'status_code': status_code,
                'status': status_text,
                'reserve': reserve_id,


            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ClientAddTimeReserve(GenericAPIView):

    """

    تعیین زمان نوبت

    """

    serializer_class = swagger_schema.AddTimeReserveSerializer
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
            ['date', 'time_range']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status_code, status_text = reserve.client_reserve_add_time(

                request.headers['Authorization'].split(' ')[-1],
                json_data,

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


class CancelTimeRange(GenericAPIView):

    """

    کنسل کردن بازه های زمانی

    """

    serializer_class = swagger_schema.CancelTimaeRangeReserveSerializer
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
            ['date', 'time_range_list']

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
            response_data, reserve_list = reserve.cancel_time_range(json_data)

            return JsonResponse({

                'status_code': 200,
                'status': 'successfully',
                'response_status': response_data,
                'reserve_list': reserve_list,

            }, status=200)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class TimeRangeList(GenericAPIView):

    """

    دریافت بازه های زمانی

    """

    # serializer_class = swagger_schema.
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        return JsonResponse({

            'status_code': 200,
            'status': 'successfully',
            'morning_time_range': [

                '8-10',
                '10-12',
                '12-14',
            ],

            'afternoon_time_range': [
                '15-17',
                '17-19',
                '19-21',
                '21-23',
                '23-1',
                '1-3',
                '3-5',

            ]

        }, status=int(200))


