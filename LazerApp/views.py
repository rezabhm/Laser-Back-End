from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, laser_app
from rest_framework.permissions import AllowAny

from . import models, serializer, swagger_schema


# Create your views here.


class LaserAreaList(GenericAPIView):

    """

    return Laser Area List

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    def get(self, request, token, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=token,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # list of laser list
            laser_area_list = models.LaserAreaInformation.objects.filter(end_time_int=0.0)

            # serializer
            laser_serializer = serializer.LaserAreaInformation(data=laser_area_list, many=True)
            laser_serializer.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ...',
                'laser_area_list': laser_serializer.data,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class AddNewLaserArea(GenericAPIView):

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
            ['token', 'name', 'price', 'deadline_reset', 'operate_time']

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
            status_code, status_text = laser_app.add_new_laser_area(

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


class EditLaserArea(GenericAPIView):

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
            ['token', 'name', 'price']

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
            status_code, status_text = laser_app.edit_new_laser_area(

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


class DeleteLaserArea(GenericAPIView):

    serializer_class = swagger_schema.DeleteLaserArea
    permission_classes = (AllowAny,)
    allowed_methods = ('DELETE',)

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
            ['token', 'name']

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
            status_code, status_text = laser_app.delete_laser_area(

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
