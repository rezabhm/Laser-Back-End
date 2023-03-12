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


class ReserveSerializer(serializers.Serializer):

    reserve = serializers.CharField()


class AddTimeReserveSerializer(serializers.Serializer):

    date = serializers.CharField()
    time_range = serializers.CharField()

class EditReserveSerializer(serializers.Serializer):

    reserve = serializers.CharField()
    laser_area_list = serializers.ListField()

class PendingReserveSerializer(serializers.Serializer):

    laser_area_list = serializers.ListField()