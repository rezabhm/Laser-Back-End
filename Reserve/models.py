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


class ReserveSchedule(models.Model):

    """

    this table will store all reserve schedule time

    """

    # information
    id = models.CharField(max_length=128, primary_key=True)

    # time information
    date = models.CharField(max_length=10)
    date_type = models.CharField(max_length=1, choices=(

        ('m', 'morning'),
        ('a', 'afternoon'),

    ))

    time_range = models.CharField(max_length=10, choices=(

        ('8-10', '8-10'),
        ('10-12', '10-12'),
        ('12-14', '12-14'),
        ('15-17', '15-17'),
        ('17-19', '17-19'),
        ('19-21', '19-21'),
        ('21-23', '21-23'),
        ('23-1', '23-1'),
        ('1-3', '1-3'),
        ('3-5', '3-5'),

    ))

    # determine total reserve time
    total_reserve_time = models.FloatField(default=0.0)

    # foreign key
    operator = models.ForeignKey(core_model.User, on_delete=models.PROTECT)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return f'{self.date}_{self.date_type}_{self.time_range}'
