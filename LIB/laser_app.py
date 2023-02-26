import time
from uuid import uuid4

from LazerApp import models
from . import utils


def add_new_laser_area(json_data):

    """

    add new laser area

    """

    try:

        # create object
        laser_object = models.LaserArea()

        # set param
        laser_object.name = json_data['name']
        laser_object.current_price = json_data['price']
        laser_object.deadline_reset = json_data['deadline_reset']
        laser_object.operate_time = json_data['operate_time']

        # save
        laser_object.save()

        # laser information
        laser_object_information = models.LaserAreaInformation()

        # set parameter
        laser_object_information.id = str(uuid4().int)
        laser_object_information.price = json_data['price']
        laser_object_information.start_time_int = time.time()
        laser_object_information.start_time_str = utils.time_int2str(time.time())
        laser_object_information.operate_time = json_data['operate_time']
        laser_object_information.laser = laser_object

        # save
        laser_object_information.save()

        return 200, 'successfully create'

    except:

        return 400, 'wrong laser area name'


def edit_new_laser_area(json_data):
    """

    add new laser area

    """

    try:

        # create object
        laser_object = models.LaserArea.objects.get(name=json_data['name'])

        # set param
        laser_object.current_price = json_data['price']

        # save
        laser_object.save()

        # laser information
        laser_object_information = models.LaserAreaInformation.objects.filter(laser__name=json_data['name']).get(
            end_time_int=0.0)

        # set parameter
        laser_object_information.end_time_int = time.time()
        laser_object_information.end_time_str = utils.time_int2str(time.time())

        # save
        laser_object_information.save()

        # laser information
        laser_object_information = models.LaserAreaInformation()

        # set parameter
        laser_object_information.id = str(uuid4().int)
        laser_object_information.price = json_data['price']
        laser_object_information.start_time_int = time.time()
        laser_object_information.start_time_str = utils.time_int2str(time.time())
        laser_object_information.operate_time = laser_object.operate_time
        laser_object_information.laser = laser_object

        # save
        laser_object_information.save()

        return 200, 'successfully create'

    except:

        return 400, 'wrong laser area name'


def delete_laser_area(json_data):
    """

    add new laser area

    """

    try:

        # create object
        laser_object = models.LaserArea.objects.get(name=json_data['name'])

        # delete
        laser_object.delete()

        return 200, 'successfully delete'

    except:

        return 400, 'wrong laser area name'
