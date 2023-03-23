import time
import uuid

from . import utils, core
from Reserve import models, serializer
from LazerApp import serializer as laser_serializer
from LazerApp import models as laser_model
from Core import models as core_model
from Payment import models as pay_model
from Payment import serializer as pay_serial
from Admin import models as admin_model


def reserve_list(json_data):

    """

    return reserve list

    """

    if json_data['from_'] == '':

        from_time = utils.time_int2str(time.time()).split(' ')[0]
        from_time = utils.cvt_solar_date2ad_int(from_time)

        to_time = from_time + (60*60*24)

    else:

        from_time = json_data['from_']
        from_time = utils.cvt_solar_date2ad_int(from_time)

        to_time = json_data['to']
        to_time = utils.cvt_solar_date2ad_int(to_time)

    all_reserve_object_list = models.Reserve.objects.filter(

        reserve_time_int__gte=from_time).filter(
        reserve_time_int__lte=to_time
    )

    complete_reserve_object_list = models.Reserve.objects.filter(

        reserve_time_int__gte=from_time).filter(
        reserve_time_int__lte=to_time).exclude(reserve_type='wa')

    uncomplete_reserve_object_list = models.Reserve.objects.filter(

        reserve_time_int__gte=from_time).filter(
        reserve_time_int__lte=to_time
    ).filter(reserve_type='wa')

    all_reserve_object_list_serializer = serializer.ReserveSerializer(data=all_reserve_object_list, many=True)
    complete_reserve_object_list_serializer = serializer.ReserveSerializer(data=complete_reserve_object_list, many=True)
    uncomplete_reserve_object_list_serializer = serializer.ReserveSerializer(data=uncomplete_reserve_object_list, many=True)

    all_reserve_object_list_serializer.is_valid()
    complete_reserve_object_list_serializer.is_valid()
    uncomplete_reserve_object_list_serializer.is_valid()

    total_price = 0.0

    for data in all_reserve_object_list:

        if data.reserve_type not in ['ca', 'pe', 'sc']:
            total_price += data.total_price_amount

    return all_reserve_object_list_serializer.data, complete_reserve_object_list_serializer.data, uncomplete_reserve_object_list_serializer.data, len(all_reserve_object_list), len(complete_reserve_object_list), len(uncomplete_reserve_object_list), total_price


def reserve_inf(json_data):

    """

    return reserve information

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=json_data['reserve'])
        reserve = serializer.ReserveSerializer(data=[reserve], many=True)
        reserve.is_valid()

        # get payment
        payment_list = pay_model.Payment.objects.filter(reserve=reserve)
        payment_list_serializer = pay_serial.PaymentSerializer(data=payment_list, many=True)
        payment_list_serializer.is_valid()

        return 200, 'successfully', [reserve.data, payment_list_serializer.data]

    except:

        return 400, 'wrong reserve id', None


def cancel_reserve(json_data):

    """

    return reserve information

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=json_data['reserve'])

        # set parameter
        reserve.reserve_type = json_data['cancel_type']

        if json_data['cancel_type'] == 'ca':

            reserve_schedule = reserve.time_range

            total_time = 0.0

            for data in reserve.laser_area_list.all():
                total_time += data.operate_time

            reserve_schedule.total_reserve_time -= total_time

            reserve_schedule.save()

        reserve.save()

        return 200, 'successfully'


    except:

        return 400, 'wrong reserve id'


def reserve_laser_area(json_data):

    """

    return reserve information

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=json_data['reserve'])

        laser_area_list = laser_serializer.LaserAreaInformation(data=reserve.laser_area_list.all(), many=True)
        laser_area_list.is_valid()

        return 200, 'successfully', laser_area_list.data


    except:

        return 400, 'wrong reserve id', None


def edit_reserve_laser_area(json_data):

    """

    return reserve information

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=json_data['reserve'])

    except:

        return 400, 'wrong reserve id'

    try:

        new_list = []
        total_price = 0.0

        for data in json_data['laser_area_list']:

            laser_area = laser_model.LaserAreaInformation.objects.filter(laser__name=data).get(end_time_int=0.0)
            total_price += laser_area.price

            new_list.append(laser_area)

    except:

        return 400, 'wrong laser area name'

    # clear current laser area list
    reserve.laser_area_list.clear()
    reserve.total_price_amount = total_price

    for data in new_list:

        reserve.laser_area_list.add(data)

    reserve.save()

    return 200, 'successfully'


def new_reserve_reception(json_data):

    """

    return reserve information

    """
    # username
    try:

        # check user exist
        user = core_model.User.objects.get(username=json_data['username'])

        # create new reserve
        reserve = models.Reserve()

        # set parameter
        reserve.id = str(uuid.uuid4().int)
        reserve.reserve_type = 'wa'
        reserve.session_number = 1
        reserve.online_reserve = False
        reserve.total_price_amount = 0.0
        reserve.total_payment_amount = 0.0
        reserve.reserve_time_int = time.time()
        reserve.reserve_time_str = utils.time_int2str(time.time())
        reserve.user = user

        # save
        reserve.save()

        return 200, "successfully", reserve.id

    except:

        return 400, "wrong username", None


def user_reserve_list(json_data):

    """

    return reserve information

    """
    # create new reserve
    reserve = models.Reserve.objects.filter(user__username=json_data['username']).order_by('reserve_time_int')
    reserve = serializer.ReserveSerializer(data=reserve, many=True)
    reserve.is_valid()

    return reserve.data


def prove_reserve(token):

    """

    proved reserve

    """

    # get user from token
    user, _ = core.get_user_from_token(token)

    try:

        # get reserve
        reserve_obj = models.Reserve.objects.filter(user=user).get(reserve_type='pe')

        # get trust price
        with open('trust_price.txt') as fd:
            trust_price = fd.read()

        if reserve_obj.total_payment_amount > float(trust_price):

            # update param
            reserve_obj.reserve_type = 'wa'

            # save
            reserve_obj.save()

            return 200, 'successfully ...'

        return 400, "you didn't pay trust price"

    except:

        return 400, "you didn't have pending reserve"


def time_list(reserve_id):

    """

    return time_list

    """

    month_cvt = {

        '1': 'فروردین',
        '2': 'اردیبهشت',
        '3': 'خرداد',

        '4': 'تیر',
        '5': 'مرداد',
        '6': 'شهریور',

        '7': 'مهر',
        '8': 'آبان',
        '9': 'آذر',

        '10': 'دی',
        '11': 'بهمن',
        '12': 'اسفند',

    }

    try:

        reserve_obj = models.Reserve.objects.get(id=reserve_id)
        reserve_body_list = reserve_obj.laser_area_list.all()
        reserve_time = 0.0

        for laser_body in reserve_body_list:

            reserve_time += laser_body.operate_time

        time_need = 120 - reserve_time

    except:

        return 400, 'wrong reserve id', None

    cu_time_int = time.time()

    json_response = []

    time_range = (

        ('8-10', '8-10', 'm'),
        ('10-12', '10-12', 'm'),
        ('12-14', '12-14', 'm'),
        ('15-17', '15-17', 'a'),
        ('17-19', '17-19', 'a'),
        ('19-21', '19-21', 'a'),
        ('21-23', '21-23', 'a'),
        ('23-1', '23-1', 'a'),
        ('1-3', '1-3', 'a'),
        ('3-5', '3-5', 'a'),

    )

    for day in range(5):

        # get day's data
        # morning time

        cu_time_int += (60*60*24)
        cu_time = utils.time_int2str(cu_time_int).split(' ')
        cu_date = cu_time[0].split('/')

        for (time_, _, date_type) in time_range:

            try:

                _ = models.ReserveSchedule.objects.filter(date=cu_time[0]).get(time_range=time_)

            except:

                operator_list = admin_model.OperatorProgram.objects.filter(date_str=cu_time[0]).filter(program_turn=date_type)
                unknown_user = core_model.User.objects.get(username='unknown')
                operator = operator_list[0] if len(operator_list) > 0 else unknown_user

                reserve_schedule_obj = models.ReserveSchedule(

                    id=str(uuid.uuid4().int),
                    date=cu_time[0],
                    date_type=date_type,
                    time_range=time_,
                    operator=operator,

                )

                # save
                reserve_schedule_obj.save()

        date_str = f'{cu_date[-1]} {month_cvt[cu_date[1]]}'
        day_str = cu_time[1]

        morning_time = models.ReserveSchedule.objects.filter(date_type='m').filter(date=cu_time[0]).filter(
            total_reserve_time__lte=time_need)

        morning_operator = f'{morning_time[0].operator.name} {morning_time[0].operator.last_name}'

        morning_time = [data.time_range for data in morning_time]

        afternoon_time = models.ReserveSchedule.objects.filter(date_type='a').filter(date=cu_time[0]).filter(
            total_reserve_time__lte=time_need)

        afternoon_operator = f'{afternoon_time[0].operator.name} {afternoon_time[0].operator.last_name}'

        afternoon_time = [data.time_range for data in afternoon_time]

        json_response.append({

            'date': date_str,
            'date_id': cu_time[0],
            'day': day_str,
            'morning_operator': morning_operator,
            'afternoon_operator': afternoon_operator,
            'morning_time': morning_time,
            'afternoon_time': afternoon_time,
            'time_length': len(morning_time) + len(afternoon_time),

        })

    return 200, 'successfully ...', json_response


def client_reserve_pending(token, laser_area_list):

    """

    create pending reserve for client

    """

    user, _ = core.get_user_from_token(token)

    if user is None:

        return 400, 'wrong token/username', None

    try:

        _ = models.Reserve.objects.filter(reserve_type='pe').get(user=user)

        return 400, 'you have pending time', None

    except:

        reserve_obj = models.Reserve(

            id=str(uuid.uuid4().int),
            session_number=1,
            reserve_type='pe',
            total_payment_amount=0.0,
            total_price_amount=0.0,
            reserve_time_int=time.time(),
            reserve_time_str=utils.time_int2str(time.time()),
            user=user,

        )

    total_payment = 0.0
    laser_area_name = ''
    reserve_obj.save()

    for laser in laser_area_list:

        try:

            laser_obj = laser_model.LaserAreaInformation.objects.get(id=laser)

        except:

            reserve_obj.delete()

            return 400, 'wrong laser id', None

        total_payment += laser_obj.price
        laser_area_name += laser_obj.laser.name + ' '
        reserve_obj.laser_area_list.add(laser_obj)

    reserve_obj.total_price_amount = total_payment
    reserve_obj.laser_area_name = laser_area_name

    reserve_obj.save()

    return 200, 'successfully', reserve_obj.id


def client_reserve_add_time(token, json_date):

    """

    add time to pending reserve

    """
    user, _ = core.get_user_from_token(token)

    hour_dict = {

        '8-10': 60*60*8,
        '10-12': 60 * 60 * 10,
        '12-14': 60 * 60 * 12,
        '15-17': 60 * 60 * 15,
        '17-19': 60 * 60 * 17,
        '19-21': 60 * 60 * 19,
        '21-23': 60 * 60 * 21,
        '23-1': 60 * 60 * 23,
        '1-3': 60 * 60 * 25,
        '3-5': 60 * 60 * 27,

    }

    if user is None:

        return 400, 'wrong token/username'

    try:

        reserve = models.Reserve.objects.filter(reserve_type='pe').get(user=user)
        reserve_schedule = models.ReserveSchedule.objects.filter(date=json_date['date']).get(time_range=json_date['time_range'])

        reserve_body_list = reserve.laser_area_list.all()
        reserve_time = 0.0

        for laser_body in reserve_body_list:

            reserve_time += laser_body.operate_time

        if 120 - reserve_schedule.total_reserve_time > reserve_time:

            reserve_time_cal = utils.cvt_solar_date2ad_int(json_date['date']) + hour_dict[json_date['time_range']] + (reserve_schedule.total_reserve_time * 60)
            reserve.reserve_time_int = reserve_time_cal
            reserve.reserve_time_str = utils.time_int2str(reserve_time_cal)

            reserve_schedule.total_reserve_time += reserve_time
            reserve_schedule.save()

            reserve.time_range = reserve_schedule

            reserve.save()

            return 200, 'successfully'

        else:

            return 400, "this time range are full"

    except:

        return 400, "wrong time range or user didn't have pending reserve"


def cancel_time_range(json_data):

    """

    cancel time range

    """
    response_data = {}

    for time_range in json_data['time_range_list']:

        try:

            time_range = models.ReserveSchedule.objects.filter(date=json_data['date']).get(
                time_range=time_range)

            time_range.total_reserve_time = 120

            time_range.save()

            response_data[time_range] = True

        except:

            response_data[time_range] = False

    return response_data


def reserve_time_range(reserve_id):

    """

    reserve time range

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=reserve_id)

        date = reserve.time_range.date
        time_range = reserve.time_range.time_range

        return 200, 'successfully', date, time_range

    except:

        return 400, 'wrong reserve id', None, None


def cancel_reserve_time_range(reserve_id):

    """

    cancel reserve time range

    """

    try:

        # get reserve
        reserve = models.Reserve.objects.get(id=reserve_id)

        reserve_body_list = reserve.laser_area_list.all()
        reserve_time = 0.0

        for laser_body in reserve_body_list:

            reserve_time += laser_body.operate_time

        time_range = reserve.time_range
        time_range.total_reserve_time -= reserve_time

        reserve.time_range = None

        reserve.save()
        time_range.save()

        return 200, 'successfully'

    except:

        return 400, 'wrong reserve id'
