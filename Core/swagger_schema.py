from rest_framework import serializers

"""

we will ad swagger's schema.
this file contain POST request's parameter for swagger

"""


class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
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
    offline_number = serializers.IntegerField()

class ChangeInformationSerializer(serializers.Serializer):

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
    offline_number = serializers.IntegerField()

class AddCustomerInfSerializer(serializers.Serializer):

    name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    national_code = serializers.CharField()
    address = serializers.CharField()
    house_number = serializers.CharField()
    drug_hist = serializers.BooleanField()
    decease_hist = serializers.BooleanField()
    doctor = serializers.CharField()
    offline_number = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


class UsernameOnlySerializer(serializers.Serializer):

    username = serializers.CharField()


class CommentListSerializer(serializers.Serializer):

    seen_status = serializers.CharField()


class ProveForgotPassSerializer(serializers.Serializer):

    username = serializers.CharField()
    code = serializers.CharField()


class CustomerProveForgotPassSerializer(serializers.Serializer):

    phone_number = serializers.CharField()
    code = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):

    username = serializers.CharField()
    code = serializers.CharField()
    password = serializers.CharField()


class TokenChangePasswordSerializer(serializers.Serializer):

    password = serializers.CharField()
    old_password = serializers.CharField()


class TokenUsernameSerializer(serializers.Serializer):

    username = serializers.CharField()


class TokenPhoneNumberSerializer(serializers.Serializer):

    phone_number = serializers.CharField()

class AddCommentSerializer(serializers.Serializer):

    comment_text = serializers.CharField()


class TokenOnlySerializer(serializers.Serializer):

    pass


class WorkTimeSerializer(serializers.Serializer):

    from_ = serializers.CharField()
    to = serializers.CharField()