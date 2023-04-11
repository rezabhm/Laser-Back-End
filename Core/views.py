from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from LIB import utils
from LIB import authentication
from LIB import core

from . import models
from . import serializer
from . import swagger_schema

# Create your views here.


class SignUpCustomer(GenericAPIView):

    """

    ثیت نام مشتری توسط تمامی کاربران

    """

    serializer_class = swagger_schema.SignUpSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)
        json_data['user_type'] = 'c'

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'name', 'last_name', 'password', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor', 'offline_number', 'last_date']

        )

        if status:
            return response

        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # check customer user
            status = core.check_username(json_data['username'], user_type='c', national_code=json_data['national_code'])

            if status:

                return JsonResponse({

                    'status_code': 400,
                    'status': 'user exist ...',

                }, status=400)

            # create user
            core.create_user(json_data)

            return JsonResponse({

                'status_code': 201,
                'status': 'user successfully create ...',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class SignUpAdmin(GenericAPIView):
    """

    ثیت نام کاربران توسط مدیر

    """

    serializer_class = swagger_schema.SignUpSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'name', 'last_name', 'password', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor', 'user_type', 'offline_number', 'last_date']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # check customer user
            status = core.check_username(

                json_data['username'],
                user_type=json_data['user_type'],
                national_code=json_data['national_code']

            )

            if status:

                return JsonResponse({

                    'status_code': 400,
                    'status': 'user exist ...',

                }, status=400)

            # create user
            core.create_user(json_data)

            return JsonResponse({

                'status_code': 201,
                'status': 'user successfully create ...',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class Login(GenericAPIView):
    """

    ورود کاربران

    """

    serializer_class = swagger_schema.LoginSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'password']

        )

        if status:
            return response

        json_data['username'] = json_data['username'].lower()

        # check customer user
        status, status_txt, token, user_type = core.login(

            username=json_data['username'],
            password=json_data['password']

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,
            'token': token,
            'user_type': user_type

        }, status=int(status))


class LogOut(GenericAPIView):
    """

    ثبت حروج کاربران

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            core.logout(request.headers['Authorization'].split(' ')[-1])

            return JsonResponse({

                'status_code': 201,
                'status_text': 'logged out',

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ForgotPassword(GenericAPIView):
    """

    ارسال در خواست فراموشی رمز عبور

    """

    serializer_class = swagger_schema.UsernameOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response

        json_data['username'] = json_data['username'].lower()

        # check customer user
        status, status_txt = core.forgot_password(

            username=json_data['username'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=int(status))


class ProveForgotPassword(GenericAPIView):
    """

    تایید کد فراموشی رمز عبور

    """

    serializer_class = swagger_schema.ProveForgotPassSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'code']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check customer user
        status, status_txt = core.prove_forgot_password(

            username=json_data['username'],
            code=json_data['code'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=int(status))


class ChangePassword(GenericAPIView):
    """

    تغییر رمز عبور

    """

    serializer_class = swagger_schema.ChangePasswordSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'code', 'password']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check customer user
        status, status_txt = core.change_password(

            username=json_data['username'],
            password=json_data['password'],
            code=json_data['code'],

        )

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=int(status))


class TokenChangePassword(GenericAPIView):
    """

    تغییر رمز عبور از روی توکن

    """

    serializer_class = swagger_schema.TokenChangePasswordSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['old_password', 'password']

        )

        if status:
            return response

        # check customer user
        status, status_txt = core.token_change_password(request, json_data)

        return JsonResponse({

            'status_code': status,
            'status_text': status_txt,

        }, status=int(status))


class UserList(GenericAPIView):
    """

    لیست تمامی کاربران

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # get list of user's
            user_list = models.User.objects.all().exclude(user_type='c').exclude(user_type='a')

            # serialize query list
            user_serial = serializer.UserSerializer(data=user_list, many=True)
            user_serial.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ... ',
                'user_list': user_serial.data,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class OperatorList(GenericAPIView):
    """

    لیست اپراتور ها

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # get list of operator's
            operator_list = models.User.objects.filter(user_type='o')

            # serialize query list
            operator_serial = serializer.UserSerializer(data=operator_list, many=True)
            operator_serial.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ... ',
                'operator_list': operator_serial.data,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CustomerList(GenericAPIView):
    """

    لیست مراجعین (مشتری)

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # get list of customer's
            customer_list = models.User.objects.filter(user_type='c')
            customer_inf_list = models.Customer.objects.all()

            # serialize query list
            customer_serial = serializer.UserSerializer(data=customer_list, many=True)
            customer_serial.is_valid()

            customer_inf_serial = serializer.CustomerSerializer(data=customer_inf_list, many=True)
            customer_inf_serial.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ... ',
                'customer_list': customer_serial.data,
                'customer_information_list': customer_inf_serial.data,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CommentList(GenericAPIView):
    """

    لیست نظرات

    """

    serializer_class = swagger_schema.CommentListSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()
    @method_decorator(csrf_exempt)
    def get(self, request, page_ination=0,*args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # get list of comment
            from_page_ination = 20 * int(page_ination)
            to_page_ination = 20 * (int(page_ination)+1)

            seen_comment_list = models.Comment.objects.filter(seen=True)[from_page_ination:to_page_ination]
            unseen_comment_list = models.Comment.objects.filter(seen=False)[from_page_ination:to_page_ination]
            all_comment_list = models.Comment.objects.all()[from_page_ination:to_page_ination]

            # serialize query list
            seen_comment_serial = serializer.CommentSerializer(data=seen_comment_list, many=True)
            seen_comment_serial.is_valid()

            unseen_comment_serial = serializer.CommentSerializer(data=unseen_comment_list, many=True)
            unseen_comment_serial.is_valid()

            all_comment_serial = serializer.CommentSerializer(data=all_comment_list, many=True)
            all_comment_serial.is_valid()

            return JsonResponse({

                'status_code': 201,
                'status_text': 'successfully ... ',
                'seen_comment': seen_comment_serial.data,
                'unseen_comment': unseen_comment_serial.data,
                'all_comment': all_comment_serial.data,
                'seen_comment_length': len(seen_comment_list),
                'unseen_comment_length': len(unseen_comment_list),
                'all_comment_length': len(all_comment_list),

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CommentChangeStatus(GenericAPIView):
    """

    تغییر وضعیت کامنت به حالت خوانده شده

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()
    @method_decorator(csrf_exempt)
    def get(self, request, comment_id, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # get list of comment
            status, status_text = core.comment_change_status(comment_id)

            return JsonResponse({

                'status_code': int(status),
                'status_text':status_text,

            }, status=201)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CustomerAdd2Charge(GenericAPIView):
    """

    اضافه کردن مشتری به دوره شارژ

    """

    serializer_class = swagger_schema.TokenUsernameSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r']

        )

        if token_status == 201:

            # add customer to charge
            status_code, status_text = core.customer_add_to_charge(json_data['username'])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class DeleteUser(GenericAPIView):
    """

    حذف کاربر توسط مدیر

    """

    serializer_class = swagger_schema.TokenUsernameSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            # add customer to charge
            status_code, status_text = core.delete_user(json_data['username'])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CustomerInf(GenericAPIView):
    """

    اطلاعات مشتری

    """

    serializer_class = swagger_schema.TokenUsernameSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # get customer
            status_code, status_text, customer, customer_inf = core.customer_information(json_data['username'])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,
                'customer': customer,
                'customer_information': customer_inf,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class ChangeUserInformation(GenericAPIView):
    """

    تغییر اطلاعات کاربران

    """

    serializer_class = swagger_schema.ChangeInformationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username', 'name', 'last_name', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor', 'user_type', 'offline_number', 'last_date']
        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            # get customer
            status_code, status_text = core.change_user_information(json_data, request)

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,


            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class EnterExitOperator(GenericAPIView):
    """

    ورود خروج اپراتور ها

    """

    serializer_class = swagger_schema.TokenUsernameSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['username']

        )

        if status:
            return response
        json_data['username'] = json_data['username'].lower()

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['r', 'a']

        )

        if token_status == 201:

            status_code, status_text = core.enter_exit_operator(json_data['username'])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,


            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class AddComment(GenericAPIView):
    """

    اضافه کردن نظرات کاربران

    """

    serializer_class = swagger_schema.AddCommentSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['comment_text']

        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['r', 'a', 'c']

        )

        if token_status == 201:

            status_code, status_text = core.add_comment(json_data['comment_text'], request.headers['Authorization'].split(' ')[-1])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,


            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class CustomerLogin(GenericAPIView):

    """

    ورود مشتری

    """

    serializer_class = swagger_schema.TokenPhoneNumberSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['phone_number']

        )

        if status:
            return response

        status_code, status_text = core.customer_login(json_data['phone_number'])

        return JsonResponse({

            'status_code': status_code,
            'status_text': status_text,


        }, status=int(status_code))


class CustomerLoginProveCode(GenericAPIView):
    """

    تایید کد ورود مشتری

    """

    serializer_class = swagger_schema.CustomerProveForgotPassSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['phone_number', 'code']

        )

        if status:
            return response

        # check token is valid or not
        # token_status, token_status_text = authentication.check_token(
        #
        #     request,
        #     access_user_type=['r', 'a', 'c']
        #
        # )

        if True:

            status_code, status_text, token_code = core.customer_login_prove_code(json_data)

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,
                'token': token_code,


            }, status=int(status_code))


class AddCustomerInf(GenericAPIView):

    """

    تکمیل اطلاعات مشتری

    """

    serializer_class = swagger_schema.AddCustomerInfSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['name', 'last_name', 'phone_number', 'national_code', 'address',
             'house_number', 'drug_hist', 'decease_hist', 'doctor', 'offline_number']
        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['r', 'a', 'c']

        )

        if token_status == 201:

            status_code, status_text = core.customer_add_inf(json_data, request.headers['Authorization'].split(' ')[-1])

            return JsonResponse({

                'status_code': status_code,
                'status_text': status_text,

            }, status=int(status_code))

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class WorkTimeList(GenericAPIView):

    """

    محاسبه زمان کاری کارمندان

    """

    serializer_class = swagger_schema.WorkTimeSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def post(self, request, *args, **kwargs):

        # decode json
        json_data = utils.decode_reqeust_json(request)

        # check input json param
        status, response = authentication.check_request_json(

            json_data,
            ['from_', 'to']
        )

        if status:
            return response

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            data = core.work_time_list(json_data)

            return JsonResponse({

                'status_code': 200,
                'status_text': 'successfully',
                'response_data': data

            }, status=200)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class WorkTime(GenericAPIView):

    """

    محاسبه زمان کاری  یک کارمندان

    """

    serializer_class = swagger_schema.TokenUsernameSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, username, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a']

        )

        if token_status == 201:

            data = core.work_time(username)

            return JsonResponse({

                'status_code': 200,
                'status_text': 'successfully',
                'response_data': data

            }, status=200)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)


class GetUsername(GenericAPIView):

    """

    دریافت نام کاربری از روی توکن

    """

    serializer_class = swagger_schema.TokenOnlySerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('GET',)

    #
    # def get(self, request, *args, **kwargs):
    #
    #     return authentication.get_error_response()

    def get(self, request, *args, **kwargs):

        # check token is valid or not
        token_status, token_status_text = authentication.check_token(

            request,
            access_user_type=['a', 'r', 'c']

        )

        if token_status == 201:

            token = request.headers['Authorization'].split(' ')[-1]
            user, _ = core.get_user_from_token(token)

            return JsonResponse({

                'status_code': 200,
                'status_text': 'successfully',
                'username': user.username

            }, status=200)

        else:

            return JsonResponse({

                'status_code': token_status,
                'status': token_status_text,

            }, status=400)
