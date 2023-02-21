from Core import models
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
    user.password = authentication.passowrd_hash(data['password'])
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
        token.token_expire_time_int = time.time() + (time.time() * 60*60*24*30)
        token.token_expire_time_str = time.time() + (time.time() * 60*60*24*30)

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

        return 400, "wrong username", None

    # password
    if user.password != authentication.password_hash(password):
        return 400, "wrong password", None

    # store operator enter time
    user_enter_time(user)

    # generate token
    token = create_token(user)

    return 200, 'success', token


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
    user, _ = get_user_from_token(token)

    # add exit time
    user_exit_time(user)


def get_user_from_token(token):

    """

    get_user_from_token

    """

    try:

        token_obj = models.Token.objects.get(token_code=token)
        return token.user, token_obj

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
            fg_obj.code_generate = f'{random.randint(99999,999999)}'
            fg_obj.expire_time = time.time() + 60*10
            fg_obj.proved = False
            fg_obj.used = False

            # save
            fg_obj.save()

        except:

            # create forgot password object
            fg_obj = models.ForgotPassword()

            # set param
            fg_obj.code = f'{random.randint(99999,999999)}'
            fg_obj.code_generate = f'{random.randint(99999,999999)}'
            fg_obj.expire_time = time.time() + 60*10
            fg_obj.user = user

            # save
            fg_obj.save()

        # send sms to user
        SMS.send_forgot_password_sms(user.phone_number, fg_obj.code_generate)

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
            fg_code = models.ForgotPassword.objects.get(code_generate=code)

            if not fg_code.used and fg_code.proved:

                # change password
                user.password = authentication.password_hash(password)
                user.save()

                # expire code
                fg_code.used = True
                fg_code.save()

                return 201, 'successfully changed password'

            else:

                return 400, 'you cant use this code'

        except:

            return 400, 'wrong code'

    else:

        return 400, 'wrong username'
