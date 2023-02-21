from Core import models as core_model

import time


def check_token(token):

    # get token from DB
    token_list = core_model.Token.objects.filter(token_code=token)

    if len(token_list) > 0:

        token = token_list[0]

        if time.time() < token.token_expire_time_int:
            return 201, "your token is valid"

        else:
            return 400, "your token's time are expired"
    else:
        return 400, "your token isn't valid ."
