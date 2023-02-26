from django.http import JsonResponse

from Core import models as core_model

import time


def check_token(token, access_user_type=[]):

    """

    this function check token is valid or not

    """

    # get token from DB
    token_list = core_model.Token.objects.filter(token_code=token)

    if len(token_list) > 0:

        token = token_list[0]

        # check this user can access to this page or not
        user = token.user
        if user.user_type not in access_user_type:
            return 400, "forbidden access"

        # check token is valid or not
        if time.time() < token.token_expire_time_int:
            return 201, "your token is valid"

        else:
            return 400, "your token's time are expired"
    else:
        return 400, "your token isn't valid ."


def get_error_response():

    """

    in most of our api we only response POST request, so we must
    return error response for GET method

    """

    return JsonResponse(

        {'status_code': 400, 'operator_program': "you cant access to api with GET method"},
        status=400

    )


def check_request_json(req_json, param_list):

    """

    this function check did json request math param list or not

    """

    for key in param_list:

        if key not in req_json.keys():

            return True, JsonResponse(

                        {'status_code': 400, 'result': "invalid input parameter", 'parameter': param_list},
                        status=400

                    )

    return False, None


def check_get(request, param_list):

    """

    this function check did json request math param list or not

    """

    for key in param_list:

        if key not in request.GET.keys():

            return True, JsonResponse(

                        {'status_code': 400, 'result': "invalid input parameter", 'parameter': param_list},
                        status=400

                    )

    return False, None


def password_hash(password):

    """

    this function convert password to hash

    """

    return password
