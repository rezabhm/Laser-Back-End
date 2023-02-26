from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    token = serializers.CharField()


class OffCodeDeleteSerializer(serializers.Serializer):

    token = serializers.CharField()
    off_code = serializers.CharField()


class OffCodeCreateSerializer(serializers.Serializer):

    token = serializers.CharField()
    off_code = serializers.CharField()
    amount = serializers.FloatField()


class OffCodeAddReserveSerializer(serializers.Serializer):

    token = serializers.CharField()
    off_code = serializers.CharField()
    Reserve = serializers.CharField()


class MultiplePayment(serializers.Serializer):

    token = serializers.CharField()
    reserve = serializers.CharField()
    payment_list = serializers.ListField()
