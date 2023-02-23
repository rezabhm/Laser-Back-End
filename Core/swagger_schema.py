from rest_framework import serializers

"""

we will ad swagger's schema.
this file contain POST request's parameter for swagger

"""


class SignUpSerializer(serializers.Serializer):

    token = serializers.CharField()
    username = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    national_code = serializers.CharField()
    address = serializers.CharField()
    house_number = serializers.CharField()
    user_type = serializers.CharField()
    drug_hist = serializers.BooleanField()
    decease_hist = serializers.BooleanField()
    doctor = serializers.CharField()


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


class UsernameOnlySerializer(serializers.Serializer):

    username = serializers.CharField()


class ProveForgotPassSerializer(serializers.Serializer):

    username = serializers.CharField()
    code = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):

    username = serializers.CharField()
    code = serializers.CharField()
    password = serializers.CharField()


class TokenUsernameSerializer(serializers.Serializer):

    token = serializers.CharField()
    username = serializers.CharField()


class TokenOnlySerializer(serializers.Serializer):

    token = serializers.CharField()
