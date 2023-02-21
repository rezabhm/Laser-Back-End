from rest_framework import serializers
from . import models

"""

we will create DRF serializer for json request

"""


class OperatorProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OperatorProgram
        fields = [

            'id',
            'date_str',
            'program_turn',
            'operator_name',
            'operator',

        ]
