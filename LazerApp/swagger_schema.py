from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    pass

class CreateLaserArea(serializers.Serializer):

    price = serializers.FloatField()
    operate_time = serializers.IntegerField()
    deadline_reset = serializers.IntegerField()
    name = serializers.CharField()


class EditLaserArea(serializers.Serializer):

    price = serializers.FloatField()
    name = serializers.CharField()


class DeleteLaserArea(serializers.Serializer):

    name = serializers.CharField()
