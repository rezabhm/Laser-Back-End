from rest_framework import serializers
from . import models


class OffCodeSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.OffCode
        fields = '__all__'
