from Admin import models
from . import utils

import time

"""

we will define Admin function on here for views

"""


def operator_program_list(date_int):

    # query to database
    operator_program_query_list = []

    for data in range(7):

        # convert int time to str time
        ad_time = time.ctime(date_int)

        # split time
        time_str = ad_time.split(' ')
        if len(time_str) == 6:
            week_day, month, _, day, _, year = ad_time.split(' ')
        else:
            week_day, month, day, _, year = ad_time.split(' ')

        # get solar time
        year, month, day, _ = utils.ad2solar(int(year), month, int(day), week_day)
        date = f'{year}/{month}/{day}'

        # get data from database
        op_list = models.OperatorProgram.objects.filter(date_str=date)

        for i in op_list:
            operator_program_query_list.append(i)

        # get next day's data
        date_int += 60 * 60 * 24

    return operator_program_query_list
