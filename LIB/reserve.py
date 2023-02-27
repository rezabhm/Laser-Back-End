import time
import uuid

from . import utils
from Reserve import models, serializer
from LazerApp import serializer as laser_serializer
from LazerApp import models as laser_model
from Core import models as core_model


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

        return 200, 'successfully', reserve.data


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
    reserve = models.Reserve.objects.filter(user__username=json_data['username'])
    reserve = serializer.ReserveSerializer(data=reserve, many=True)
    reserve.is_valid()

    return reserve.data
