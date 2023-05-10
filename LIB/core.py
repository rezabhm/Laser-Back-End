from Core import models
from Core import serializer
from . import authentication
from LIB import utils
from SmsService import SMS

import random
import time
from uuid import uuid4


def check_username(username, user_type='c', national_code='0'):
    """

    check username exist or not

    """

    try:

        # user exist
        _ = models.User.objects.get(username=username)

        return True

    except:

        # didn't exist
        pass

    if user_type == 'c':

        try:

            # user exist
            _ = models.Customer.objects.get(national_code=national_code)

            return True

        except:

            # didn't exist
            return False

    return False


def create_user(data):
    """
    create user
    """

    # create object
    user = models.User()

    # set parameter
    user.username = data['username']
    user.name = data['name']
    user.last_name = data['last_name']
    user.phone_number = data['phone_number']
    user.password = authentication.password_hash(data['password'])
    user.user_type = data['user_type']

    # save
    user.save()

    if data['user_type'] == 'c':
        # create customer object
        customer = models.Customer()

        # set parameter
        customer.national_code = data['national_code']
        customer.address = data['address']
        customer.house_number = data['house_number']
        customer.drug_hist = data['drug_hist']
        customer.decease_hist = data['decease_hist']
        customer.doctor = data['doctor']
        customer.offline_num = data['offline_number']
        customer.last_date = data['last_date']
        customer.user = user

        # save
        customer.save()


def create_token(user):
    """

    create token

    """

    try:

        # check token exist
        token = models.Token.objects.filter(token_expire_time_int__gte=time.time()).get(user=user)

    except:

        # create token
        token = models.Token()

        # set param
        token.user = user
        token.token_code = uuid4().hex
        token.token_create_time_int = time.time()
        token.token_create_time_str = utils.time_int2str(time.time())
        token.token_expire_time_int = time.time() + (time.time() * 60 * 60 * 24 * 30)
        token.token_expire_time_str = time.time() + (time.time() * 60 * 60 * 24 * 30)

        # save
        token.save()

    return token.token_code


def login(username, password):
    """

    login user

    """

    # username
    try:

        # check user exist
        user = models.User.objects.get(username=username)

    except:

        return 400, "wrong username", None, None

    # password
    if user.password != authentication.password_hash(password):
        return 400, "wrong password", None, None

    # store operator enter time
    user_enter_time(user)

    # generate token
    token = create_token(user)

    return 200, 'success', token, user.user_type


def user_enter_time(user):
    """

    store user's enter time

    """

    if user.user_type in ['r', 'o']:
        # create enter model
        enter_ob = models.EmployeeEnterExit()

        # set param
        enter_ob.id = str(uuid4().int)
        enter_ob.enter_time_int = time.time()
        enter_ob.enter_time_str = utils.time_int2str(time.time())
        enter_ob.user = user

        # save
        enter_ob.save()


def user_exit_time(user):
    """

    store user's enter time

    """

    if user.user_type in ['r', 'o']:

        try:

            # create enter model
            exit_ob = models.EmployeeEnterExit.objects.filter(exited=False).order_by('enter_time_int')[-1]

            # set param
            exit_ob.exited = True
            exit_ob.exit_time_int = time.time()
            exit_ob.exit_time_str = utils.time_int2str(time.time())

            # save
            exit_ob.save()

        except:
            pass


def logout(token):
    """

    store user's exit time

    """

    # get user
    user, token = get_user_from_token(token)

    # token.token_expire_time_int = time.time()
    # token.save()
    token.delete()

    # add exit time
    user_exit_time(user)


def get_user_from_token(token):
    """

    get_user_from_token

    """

    try:

        token_obj = models.Token.objects.get(token_code=token)
        return token_obj.user, token_obj

    except:

        return None, None


def forgot_password(username):
    """

    create forgot password code

    """

    # check username
    status = check_username(username, '', '')

    if status:

        # get user
        user = models.User.objects.get(username=username)

        try:

            # get forgot password
            fg_obj = models.ForgotPassword.objects.get(user=user)

            # update param
            fg_obj.code_generate = f'{random.randint(99999, 999999)}'
            fg_obj.expire_time = time.time() + 60 * 10
            fg_obj.proved = False
            fg_obj.used = False

            SMS.send_password_code_sms(user.phone_number, fg_obj.code_generate)

            # save
            fg_obj.save()

        except:

            # create forgot password object
            fg_obj = models.ForgotPassword()

            # set param
            fg_obj.code = f'{random.randint(99999, 999999)}'
            fg_obj.code_generate = f'{random.randint(99999, 999999)}'
            fg_obj.expire_time = time.time() + 60 * 10
            fg_obj.user = user

            # save
            fg_obj.save()

        return 201, 'successfully'

    else:

        return 400, 'wrong username'


def prove_forgot_password(username, code):
    """

    check forgot password's code is valid or not

    """

    # check username
    status = check_username(username, '', '')

    if status:

        try:

            # check code
            fg_code = models.ForgotPassword.objects.get(code_generate=code)

            if fg_code.expire_time >= time.time():

                fg_code.proved = True
                fg_code.save()

                return 201, 'proved'

            else:

                return 400, 'time limit exceed'

        except:

            return 400, 'wrong code'

    else:

        return 400, 'wrong username'


def change_password(username, password, code):
    """

    check forgot password's code is valid or not

    """

    # check username
    status = check_username(username, '', '')

    if status:

        # get user
        user = models.User.objects.get(username=username)

        try:

            # check code
            fg_code = models.ForgotPassword.objects.filter(user=user).get(code_generate=code)

            if not fg_code.used:

                # change password
                user.password = authentication.password_hash(password)
                user.save()

                # expire code
                fg_code.used = True
                fg_code.save()

                return 201, 'successfully changed password'

            else:

                return 400, 'you cant use this code because you have use it'

        except:

            return 400, 'wrong code'

    else:

        return 400, 'wrong username'


def token_change_password(request, json_data):
    """

    check forgot password's code is valid or not

    """

    # check username
    user, _ = get_user_from_token(request.headers['Authorization'].split(' ')[-1])

    if user:

        if user.password == authentication.password_hash(json_data['old_password']):

            user.password = authentication.password_hash(json_data['password'])
            user.save()

            return 200, 'successfully changed'

        else:

            return 400, 'wrong old password'

    else:

        return 400, 'wrong token'


def customer_add_to_charge(username):
    """

    add customer to charge

    """

    try:

        # get customer
        customer = models.Customer.objects.get(user__username=username)

        # add to charge
        customer.charge = True

        # save
        customer.save()

        return 201, 'successfully ... '

    except:

        return 400, 'wrong username'


def delete_user(username):
    """

    add customer to charge

    """

    try:

        # get user
        user = models.User.objects.get(username=username)

        if user.user_type == 'c':

            # get user
            customer = models.Customer.objects.filter(user__username=username)

            if len(customer) > 0:

                cust = customer[0]

                # delete
                cust.delete()

        # delete
        user.delete()

        return 201, 'successfully ... '

    except:

        return 400, 'wrong username'


def customer_information(username):
    """

    add customer to charge

    """

    try:

        # get customer
        customer_inf = models.Customer.objects.get(user__username=username)
        customer = models.User.objects.get(username=username)

        # serialize
        customer_inf_serializer = serializer.CustomerSerializer(instance=customer_inf)
        customer_serializer = serializer.UserSerializer(instance=customer)

        return 201, 'successfully ... ', customer_serializer.data, customer_inf_serializer.data

    except:

        return 400, 'wrong username', None, None


def change_user_information(json_data, request):
    """

    change user's information

    """

    try:

        # get user
        user = models.User.objects.get(username=json_data['username'])
        token = models.Token.objects.get(token_code=request.headers['Authorization'].split(' ')[-1])

        if json_data['username'] == token.user.username or token.user.user_type == 'a':

            # update param
            user.phone_number = json_data['phone_number'] if len(
                str(json_data['phone_number'])) > 0 else user.phone_number
            user.name = json_data['name'] if len(str(json_data['name'])) > 0 else user.name
            user.last_name = json_data['last_name'] if len(str(json_data['last_name'])) > 0 else user.last_name
            user.user_type = json_data['user_type'] if len(str(json_data['user_type'])) > 0 and json_data[
                'user_type'] != 'a' else user.user_type

            # save
            user.save()

            if token.user.user_type == 'c':
                # customer
                customer = models.Customer.objects.get(user__username=json_data['username'])

                # set parameter
                customer.doctor = json_data['doctor']
                customer.address = json_data['address']
                customer.house_number = json_data['house_number']
                customer.drug_hist = json_data['drug_hist']
                customer.decease_hist = json_data['decease_hist']
                customer.offline_num = json_data['offline_number']
                customer.last_date = json_data['last_date']

                # save
                customer.save()

            return 201, 'successfully'

        else:

            return 400, "you didn't have access to change information"

    except:

        return 400, 'wrong username'


def enter_exit_operator(username):
    """

    record operator's enter/exit time

    """

    # check username
    try:

        user = models.User.objects.get(username=username)

    except:

        return 400, 'wrong username'

    # check user entered or didn't
    enter_exit_operator_list = models.EmployeeEnterExit.objects.filter(user__username=username).filter(exited=False)

    if len(enter_exit_operator_list) > 0:

        # this condition means we record users enter time, and we must add exit time
        exit_obj = enter_exit_operator_list[0]

        # set parameter
        exit_obj.exit_time_int = time.time()
        exit_obj.exit_time_str = utils.time_int2str(time.time())
        exit_obj.exited = True

        # save
        exit_obj.save()

    else:

        # we must record enter time
        enter_obj = models.EmployeeEnterExit()

        # set parameter
        enter_obj.id = str(uuid4().int)
        enter_obj.enter_time_int = time.time()
        enter_obj.enter_time_str = utils.time_int2str(time.time())
        enter_obj.user = user

        # save
        enter_obj.save()

    return 201, 'successfully'


def add_comment(comment_text, token):
    """

    create new comment

    """

    # get user
    user, _ = get_user_from_token(token)

    # create comment
    comment = models.Comment(

        id=str(uuid4().int),
        comment_text=comment_text,
        create_time_int=time.time(),
        create_time_str=utils.time_int2str(time.time()),
        user=user

    )

    # save
    comment.save()

    return 200, 'successfully create'


def customer_login(username):
    """

    login customer

    """

    try:

        # get user
        user = models.User.objects.get(username=username)

        # get login code
        login_code = models.ForgotPassword.objects.get(user=user)

        # set param
        login_code.code_generate = f'{random.randint(99999, 999999)}'
        login_code.expire_time = time.time() + (60 * 10)
        login_code.used = False
        login_code.proved = False

        SMS.send_password_code_sms(username, login_code.code_generate)

        # save
        login_code.save()

    except:

        user_list = models.User.objects.filter(username=username)

        if len(user_list) > 0:

            user = user_list[0]

        else:
            # create user
            user = models.User(

                username=username,
                user_type='c'

            )

            # save
            user.save()

        # create prove code
        login_code = models.ForgotPassword(

            code=str(uuid4().int),
            code_generate=f'{random.randint(99999, 999999)}',
            expire_time=time.time() + (60 * 10),
            user=user

        )

        # save
        login_code.save()

    return 201, 'successfully ...'


def customer_login_prove_code(json_data):
    """

    login customer

    """

    try:

        # get user
        user = models.User.objects.get(username=json_data['phone_number'])

        # get login code
        login_code = models.ForgotPassword.objects.filter(expire_time__gte=time.time()).get(user=user)

        if json_data['code'] == login_code.code_generate:

            # update parameter
            login_code.proved = True
            login_code.used = True

            token = create_token(user)

            # save
            login_code.save()

            return 201, 'proved ...', token

        else:

            return 400, 'wrong code', None



    except:

        return 400, 'wrong code/expired time', None


def customer_add_inf(json_data, token):
    """

    add customer information for signup

    """

    user, _ = get_user_from_token(token)

    if user:

        user, _ = get_user_from_token(token)

        # set parameter
        user.name = json_data['name']
        user.last_name = json_data['last_name']
        user.phone_number = json_data['phone_number']

        # save
        user.save()

        try:

            # create customer object
            customer = models.Customer.objects.get(user=user)

        except:

            customer = models.Customer()
            customer.user = user

        # set parameter
        customer.national_code = json_data['national_code']
        customer.address = json_data['address']
        customer.house_number = json_data['house_number']
        customer.drug_hist = json_data['drug_hist']
        customer.decease_hist = json_data['decease_hist']
        customer.doctor = json_data['doctor']
        customer.offline_num = json_data['offline_number']

        # save
        customer.save()

        return 200, 'successfully'

    else:

        return 400, 'wrong token'


def work_time_list(json_data):
    """

    employer work time

    """

    from_time = json_data['from_']
    from_time = utils.cvt_solar_date2ad_int(from_time)

    to_time = json_data['to']
    to_time = utils.cvt_solar_date2ad_int(to_time)

    employer_time = models.EmployeeEnterExit.objects.filter(exited=True).filter(enter_time_int__gte=from_time).filter(
        enter_time_int__lte=to_time)

    final_data = {}

    for data in employer_time:
        if data.user.username not in final_data.keys():
            final_data[data.user.username] = {

                'morning_time': 0.0,
                'afternoon_time': 0.0,

            }

        data_hour = int(data.enter_time_str.split(' ')[-1].split(':')[0])
        if (data_hour < 14) and (data_hour > 8):

            # add with morning time
            final_data[data.user.username]['morning_time'] += (data.exit_time_int - data.enter_time_int)

        else:

            # add with afternoon time
            final_data[data.user.username]['afternoon_time'] += (data.exit_time_int - data.enter_time_int)

    return final_data


def work_time(username):
    """

    employer work time

    """

    employer_time = models.EmployeeEnterExit.objects.filter(exited=True).filter(user__username=username)
    final_data = serializer.EmployeeEnterExitSerializer(data=employer_time, many=True)
    final_data.is_valid()

    return final_data.data


def comment_change_status(comment_id):

    """

    change comment id

    """

    try:

        # get comment
        comment = models.Comment.objects.get(id=comment_id)

        comment.seen = True

        comment.save()

        return 200, 'successfully ..'

    except:

        return 400, 'wrong comment id'

