from rest_framework import serializers


class TokenOnlySerializer(serializers.Serializer):

    token = serializers.CharField()
