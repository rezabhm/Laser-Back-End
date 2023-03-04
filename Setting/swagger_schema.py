from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    pass

class AddSetting(serializers.Serializer):

    trust_price = serializers.FloatField()
    morning_time = serializers.IntegerField()
    afternoon_time = serializers.IntegerField()
