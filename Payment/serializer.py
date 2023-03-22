from rest_framework import serializers
from . import models


class OffCodeSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.OffCode
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Payment
        fields = '__all__'
