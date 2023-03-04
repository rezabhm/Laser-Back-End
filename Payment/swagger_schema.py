from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    pass

class OffCodeDeleteSerializer(serializers.Serializer):

    off_code = serializers.CharField()


class OffCodeCreateSerializer(serializers.Serializer):

    off_code = serializers.CharField()
    amount = serializers.FloatField()


class OffCodeAddReserveSerializer(serializers.Serializer):

    off_code = serializers.CharField()
    Reserve = serializers.CharField()


class MultiplePayment(serializers.Serializer):

    reserve = serializers.CharField()
    payment_list = serializers.ListField()
