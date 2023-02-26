from rest_framework import serializers
from . import models


class LaserArea(serializers.ModelSerializer):

    class Meta:

        model = models.LaserArea
        fields = '__all__'


class LaserAreaInformation(serializers.ModelSerializer):

    class Meta:

        model = models.LaserAreaInformation
        fields = '__all__'
