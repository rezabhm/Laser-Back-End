from django.db import models
from Reserve import models as res_model


# Create your models here.
class ZarinPall(models.Model):

    authority = models.CharField(max_length=100, primary_key=True)
    amount = models.FloatField(default=0)
    ref_id = models.FloatField(default=0)

    status = models.CharField(max_length=15, choices=(

        ('pending', 'pending'),
        ('Successfully', 'Successfully'),
        ('Fail', 'Fail'),

    ), default='pending')

    reserve = models.ForeignKey(res_model.Reserve, on_delete=models.PROTECT)

    def __str__(self):
        return self.authority
