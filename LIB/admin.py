from Admin import models
from Core import models as core_model

from . import utils

import time

"""

we will define Admin function on here for views

"""


def operator_program_list(date_int):

    """

    this function get arbitrary date and return 7 next day's operator program that scheduled

    """

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


def check_program(operator_program):

    """

    this function get operator program and check this program exist or not.
    if exist it must update its data.

    input data format :

        operator program = {

            date: "string"          ==> show date of program                        $ example : '1401/1101'
            operator: "string"      ==> operator's username                         $ example : 'Reza'
            program_turn : "string" ==> define program is on morning or afternoon   $ example : 'm'
            operator_name: "String" ==> operator operator name                      $ example : 'reza'

        }

    """

    # get id
    id_ = operator_program['date'] + operator_program['program_turn']

    try:

        # program exist in this statement
        op = models.OperatorProgram.objects.get(id=id_)

        return op, True

    except:

        # program didn't exist
        return None, False


def create_operator_program(operator_program):

    """

    create new operator program

    input data format :

        operator program = {

            date: "string"          ==> show date of program                        $ example : '1401/1101'
            operator: "string"      ==> operator's username                         $ example : 'Reza'
            program_turn : "string" ==> define program is on morning or afternoon   $ example : 'm'
            operator_name: "String" ==> operator operator name                      $ example : 'reza'

        }


    """

    # create operator program
    op = models.OperatorProgram()
    id_ = operator_program['date'] + operator_program['program_turn']

    # set param
    op.id = id_
    op.operator_name = operator_program['operator_name']
    op.program_turn = operator_program['program_turn']
    op.date_int = utils.cvt_solar_date2ad_int(operator_program['date'])
    op.date_str = operator_program['date']

    try:

        # user exist
        user = core_model.User.objects.get(username=operator_program['operator'])

        # change operator
        op.operator = user

    except:

        # user didn't exist
        return False, f"operator {operator_program['operator']} didn't exist ..."

    # save
    op.save()

    return True,  f"Create operator {operator_program['operator']} successfully ..."


def update_operator_program(op, operator_program):

    """

    update operator program

    input data format :

        operator program = {

            date: "string"          ==> show date of program                        $ example : '1401/1101'
            operator: "string"      ==> operator's username                         $ example : 'Reza'
            program_turn : "string" ==> define program is on morning or afternoon   $ example : 'm'
            operator_name: "String" ==> operator operator name                      $ example : 'reza'

        }

    """

    # update data

    # check operator's name
    if operator_program['operator_name'] != op.operator_name:
        # update it
        op.operator_name = operator_program['operator_name']

    # check username
    if operator_program['operator'] != op.operator.username:

        # update it
        # get user
        try:

            # user exist
            user = core_model.User.objects.get(username=operator_program['operator'])

            # change operator
            op.operator = user

        except:

            # user didn't exist
            return False, f"operator {operator_program['operator']} didn't exist ..."

    # save changes
    op.save()

    return True, f"Update operator {operator_program['operator']} successfully ..."


def uc_program(op, op_model, cp_status):

    """

    this function update or create operator program

    """

    if cp_status:

        # program exist
        # we must update it
        status, status_text = update_operator_program(op_model, op)

        # add result to operator program dict for response
        op['res_status'] = status
        op['res'] = status_text

    else:

        # program didn't exist
        # we must create it
        status, status_text = create_operator_program(op)

        # add result to operator program dict for response
        op['res_status'] = status
        op['res'] = status_text

    return op


def week_time(week_day):

    """

    return week's date

    """

    week = {

        'Sat': 0,
        'Sun': 1,
        'Mon': 2,
        'Tue': 3,
        'Wed': 4,
        'Thu': 5,
        'Fri': 6,

    }

    current = time.time() + (int(week_day) * 7 * 24 * 60 * 60)

    day = time.ctime(current).split(' ')[0]

    now = utils.time_int2str(current).split(' ')[0]
    now = utils.cvt_solar_date2ad_int(now) - (week[day] * 60 * 60 * 24)
    now = utils.time_int2str(now).split(' ')[0]

    return now
