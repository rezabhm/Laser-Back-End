from django.db import models

# Create your models here.


class LaserArea(models.Model):

    """

    this table will save laser's area

    """

    # information
    name = models.CharField(max_length=50, primary_key=True)
    current_price = models.FloatField(default=0.0)

    # this param define after how many day's we must reset laser operation session (day)
    deadline_reset = models.IntegerField(default=30)

    # this param determine operate time (minute)
    operate_time = models.IntegerField(default=5)

    def __str__(self):
        return self.name


class LaserAreaInformation(models.Model):

    """

    define different time and price of laser area

    """

    # information
    id = models.CharField(max_length=128, primary_key=True)
    price = models.FloatField(default=0.0)

    # timing
    start_time_int = models.FloatField(default=0.0)
    start_time_str = models.CharField(default='-', max_length=25)

    end_time_int = models.FloatField(default=0.0)
    end_time_str = models.CharField(default='-', max_length=25)

    # this param determine operate time (minute)
    operate_time = models.IntegerField(default=5)

    # foreign key
    laser = models.ForeignKey(LaserArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.laser.name
