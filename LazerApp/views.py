from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, laser_app
from rest_framework.permissions import AllowAny

from . import models, serializer, swagger_schema


# Create your views here.


class LaserAreaList(GenericAPIView):

    """

    لیست نواحی لیزر

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # list of laser list
            laser_area_list = models.LaserAreaInformation.objects.filter(end_time_int=0.0).filter(laser__status=True)
            all_laser_area_list = models.LaserAreaInformation.objects.filter(end_time_int=0.0)

            # serializer
            laser_serializer = serializer.LaserAreaInformation(data=laser_area_list, many=True)
            laser_serializer.is_valid()

            all_laser_serializer = serializer.LaserAreaInformation(data=all_laser_area_list, many=True)
            all_laser_serializer.is_valid()

            laser_list_object = []
            laser_list_object_2 = []
            for data in laser_area_list:

                laser_list_object.append({

                    'value': data.id,
                    'label': data.laser.name,
                    'operate_time': data.operate_time,
                    'price': data.price

                })

                laser_list_object_2.append({

                    'value': data.laser.name,
                    'label': data.laser.name,
                    'operate_time': data.operate_time,
                    'price': data.price

                })

            all_laser_list_object = []
            all_laser_list_object_2 = []
            for data in all_laser_area_list:
                all_laser_list_object.append({

                    'value': data.id,
                    'label': data.laser.name,
                    'operate_time': data.operate_time,
                    'price': data.price

                })

                all_laser_list_object_2.append({

                    'value': data.laser.name,
                    'label': data.laser.name,
                    'operate_time': data.operate_time,
                    'price': data.price

                })

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ...',
                'laser_area_object': {

                    'first_type': laser_list_object,
                    'second_type': laser_list_object_2

                },

                'all_laser_area_object': {

                    'first_type': all_laser_list_object,
                    'second_type': all_laser_list_object_2,

                },

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class AddNewLaserArea(GenericAPIView):
    """

    اضافه کردن ناحیه جدید

    """

    serializer_class = swagger_schema.CreateLaserArea
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
            ['name', 'price', 'deadline_reset', 'operate_time']

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
            status_code, status_text = laser_app.add_new_laser_area(

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


class EditLaserArea(GenericAPIView):
    """

    ویرایش اطلاعات ناحیه لیزر

    """

    serializer_class = swagger_schema.EditLaserArea
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
            ['name', 'price']

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
            status_code, status_text = laser_app.edit_new_laser_area(

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


class ChangeLaserAreaStatus(GenericAPIView):
    """

    تغییر وضعیت ناحیه لیزر

    """

    serializer_class = swagger_schema.DeleteLaserArea
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
            ['name']

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
            status_code, status_text = laser_app.delete_laser_area(

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
