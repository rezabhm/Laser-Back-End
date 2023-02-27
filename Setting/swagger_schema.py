from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    token = serializers.CharField()


class AddSetting(serializers.Serializer):

    token = serializers.CharField()
    trust_price = serializers.FloatField()
    morning_time = serializers.IntegerField()
    afternoon_time = serializers.IntegerField()
