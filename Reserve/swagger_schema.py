from rest_framework import serializers


class ReserveListSerializer(serializers.Serializer):

    token = serializers.CharField()
    from_ = serializers.CharField()
    to = serializers.CharField()


class ReserveInformationSerializer(serializers.Serializer):

    token = serializers.CharField()
    reserve = serializers.CharField()


class NewReserveSerializer(serializers.Serializer):

    token = serializers.CharField()
    username = serializers.CharField()


class CancelReserveSerializer(serializers.Serializer):

    token = serializers.CharField()
    reserve = serializers.CharField()
    cancel_type = serializers.CharField()
