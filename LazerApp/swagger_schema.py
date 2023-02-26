from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    token = serializers.CharField()


class CreateLaserArea(serializers.Serializer):

    token = serializers.CharField()
    price = serializers.FloatField()
    operate_time = serializers.IntegerField()
    deadline_reset = serializers.IntegerField()
    name = serializers.CharField()


class EditLaserArea(serializers.Serializer):

    token = serializers.CharField()
    price = serializers.FloatField()
    name = serializers.CharField()


class DeleteLaserArea(serializers.Serializer):

    token = serializers.CharField()
    name = serializers.CharField()
