from rest_framework import serializers
from . import models


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Reserve
        fields = '__all__'
