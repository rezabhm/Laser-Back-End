from rest_framework import serializers

"""

we will ad swagger's schema.
this file contain POST request's parameter for swagger

"""


class OperatorProgramListSerializer(serializers.Serializer):

    token = serializers.CharField()
    date_year = serializers.IntegerField()
    date_month = serializers.IntegerField()
    date_day = serializers.IntegerField()


class OperatorProgramSerializer(serializers.Serializer):

    date = serializers.CharField()
    operator = serializers.CharField()
    program_turn = serializers.CharField()
    operator_name = serializers.CharField()


class SetOperatorSerializer(serializers.Serializer):

    token = serializers.CharField()
    operator_program_list = serializers.ListSerializer(child=serializers.DateField())


class WeekTime(serializers.Serializer):

    week = serializers.IntegerField()
