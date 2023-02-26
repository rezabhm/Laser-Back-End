import time

from Admin import models
from . import utils


def operator():

    """
    return current operator

    """

    current_time = time.time()
    current_time_str = time.ctime(current_time).split(' ')
    current_time_str_pe = utils.time_int2str(current_time).split(' ')[0]
    current_time_str_type = current_time_str[-2].split(':')[0]

    time_type = 'm' if float(current_time_str_type) > 15 else 'a'

    # get current operator program
    opp_obj = models.OperatorProgram.objects.get(id=current_time_str_pe + time_type)

    try:

        return 200, 'successfully', {

            'username': opp_obj.operator.username,
            'name': f'{opp_obj.operator.name} {opp_obj.operator.last_name}',

        }

    except:

        return 400, "didn't set operator", {

            'username': 'UnKnown',
            'name': 'UnKnown',

        }
