from rest_framework import serializers
from . import models

"""

we will create DRF serializer for json request

"""


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [

            'username',
            'name',
            'last_name',
            'phone_number',
            'user_type'

        ]


class EmployeeEnterExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmployeeEnterExit
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'
