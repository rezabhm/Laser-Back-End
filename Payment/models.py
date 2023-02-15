from django.db import models
from Config import config
from Core import models as core_model
from Reserve import models as res_model

# Create your models here.


class Payment(models.Model):

    """

    store user's payment

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)
    price = models.FloatField(default=0.0)

    # timing
    payment_time_int = models.FloatField(default=0.0)
    payment_time_str = models.CharField(default='-', max_length=25)

    # payment type
    payment_type = models.CharField(max_length=2, choices=config.payment_type_tuple)

    # foreign key
    user = models.ForeignKey(core_model.User, on_delete=models.PROTECT)
    reserve = models.ForeignKey(res_model.Reserve, on_delete=models.PROTECT)

    def __str__(self):
        return self.id


class OffCode(models.Model):

    """

    store off code for payment

    """

    # information
    code = models.CharField(max_length=10, primary_key=True)
    amount = models.FloatField()
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code
