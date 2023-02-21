from django.db import models

from Core import models as core_models

# Create your models here.


class OperatorProgram(models.Model):

    """

    this is table store operator's program to determine every reserve's operator.
    in this table we only save every turn's operator that admin determines its user

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)
    operator_name = models.CharField(max_length=20, default='UnKnow', null=True)

    # program date
    date_int = models.FloatField(default=0.0)
    date_str = models.CharField(default='-', max_length=50)

    # program time
    program_turn_tuple = (

        ('m', 'morning'),
        ('a', 'afternoon'),

    )
    program_turn = models.CharField(max_length=1, choices=program_turn_tuple, default='m')

    # foreign key
    operator = models.ForeignKey(core_models.User, on_delete=models.PROTECT, default='', null=True)

    def __str__(self):
        return self.id


class CancelTime(models.Model):

    """

    store every time that admin cancel . that mean we must cancel all reservation and didn't let anyone reserve

    """

    id = models.CharField(max_length=150, primary_key=True)

    # start cancel range
    start_time_int = models.FloatField(default=0.0)
    start_time_str = models.CharField(max_length=50)

    # end cancel range
    end_time_int = models.FloatField(default=0.0)
    end_time_str = models.CharField(max_length=50)

    def __str__(self):
        return self.id
