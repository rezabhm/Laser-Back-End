from rest_framework import serializers


class ReserveListSerializer(serializers.Serializer):

    from_ = serializers.CharField()
    to = serializers.CharField()


class ReserveInformationSerializer(serializers.Serializer):

    reserve = serializers.CharField()


class NewReserveSerializer(serializers.Serializer):

    username = serializers.CharField()


class CancelReserveSerializer(serializers.Serializer):

    reserve = serializers.CharField()
    cancel_type = serializers.CharField()
