from rest_framework import serializers
from . import models

"""

we will create DRF serializer for json request

"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [

            'id',
            'date_str',
            'program_turn',
            'operator_name',
            'operator',

        ]
