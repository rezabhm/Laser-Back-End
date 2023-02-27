from django.db import models
from Core import models as core_model
from LazerApp import models as laser_model
from Config import config

# Create your models here.


class Reserve(models.Model):

    """
     
    store all user's reservation

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)
    session_number = models.IntegerField()
    reserve_type = models.CharField(max_length=2, choices=config.reservation_type_tuple)

    # status
    online_reserve = models.BooleanField(default=True)
    charge = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    used_off_code = models.BooleanField(default=False)

    # price
    total_price_amount = models.FloatField()
    total_payment_amount = models.FloatField()

    # timing
    reserve_time_int = models.FloatField(default=0.0)
    reserve_time_str = models.CharField(default='-', max_length=25)

    request_time_int = models.FloatField(default=0.0)
    request_time_str = models.CharField(default='-', max_length=25)

    # foreign key
    user = models.ForeignKey(core_model.User, on_delete=models.PROTECT)
    off_code = models.CharField(max_length=10, null=True)
    laser_area = models.ForeignKey(laser_model.LaserArea, on_delete=models.PROTECT, null=True)
    laser_area_list = models.ManyToManyField(laser_model.LaserAreaInformation)
    laser_area_name = models.TextField(default='-', max_length=25)

    def __str__(self):
        return self.id


class PreReserve(models.Model):

    """

    store user's previous offline session information

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)
    reserve_num = models.IntegerField()
    last_date = models.CharField(max_length=50)

    # foreign key
    user = models.ForeignKey(core_model.User, on_delete=models.PROTECT)
    laser_area = models.ForeignKey(laser_model.LaserAreaInformation, on_delete=models.PROTECT)

    def __str__(self):
        return self.id
