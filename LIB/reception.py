import time

from Admin import models
from Core import models as core_model
from . import utils


def operator():

    """
    return current operator

    """

    current_time = time.time()
    current_time_str = time.ctime(current_time).split(' ')
    current_time_str_pe = utils.time_int2str(current_time).split(' ')[0]
    current_time_str_type = current_time_str[-2].split(':')[0]

    time_type = 'a' if float(current_time_str_type) > 15 else 'm'
    reception = core_model.EmployeeEnterExit.objects.filter(exited=False).filter(user__user_type='r')
    operator_enter = core_model.EmployeeEnterExit.objects.filter(exited=False).filter(user__user_type='o')

    try:
        # get current operator program
        opp_obj = models.OperatorProgram.objects.get(id=current_time_str_pe + time_type)

        return 200, 'successfully', {

            'username': opp_obj.operator.username,
            'name': f'{opp_obj.operator.name} {opp_obj.operator.last_name}',
            'reception_username': reception[len(reception)-1].user.username if len(reception) > 0 else "UnKnown",
            'reception_name': f'{reception[len(reception)-1].user.name} {reception[len(reception)-1].user.last_name}' if len(reception) > 0 else "UnKnown",

            'entered_operator_username': operator_enter[len(operator_enter) - 1].user.username if len(
                operator_enter) > 0 else None,
            'entered_operator_name': f'{operator_enter[len(operator_enter) - 1].user.name} {operator_enter[len(operator_enter) - 1].user.last_name}' if len(
                operator_enter) > 0 else None,
        }

    except:

        return 400, "didn't set operator", {

            'username': 'UnKnown',
            'name': 'UnKnown',
            'reception_username': reception[len(reception) -1].user.username if len(reception) > 0 else "UnKnown",
            'reception_name': f'{reception[len(reception) -1].user.name} {reception[len(reception) -1].user.last_name}' if len(
                reception) > 0 else "UnKnown",

            'entered_operator_username': operator_enter[len(operator_enter) - 1].user.username if len(operator_enter) > 0 else None,
            'entered_operator_name': f'{operator_enter[len(operator_enter) - 1].user.name} {operator_enter[len(operator_enter) - 1].user.last_name}' if len(
                operator_enter) > 0 else None,

        }
