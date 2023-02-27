from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from LIB import utils, authentication, reception

from rest_framework.permissions import AllowAny

from . import models, serializer, swagger_schema


# Create your views here.


class Operator(GenericAPIView):

    """

    اپراتور شیفت

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    def get(self, request, token, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            token=token,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            status_code, status_text, data = reception.operator()

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,
                'operator_name': data['name'],
                'operator_username': data['username'],

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)

