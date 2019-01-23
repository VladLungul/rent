from django.db import models
from cars.choice import RENT_TYPE


class TransferOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    user_id = models.CharField(max_length=25)
    user_phonenumber = models.CharField(max_length=25)
    car_id = models.CharField(max_length=25)
    starttime = models.DateTimeField()
    city = models.CharField(max_length=25)
    owner_id = models.CharField(max_length=25)
    rent_type = models.CharField(choices=RENT_TYPE, max_length=25)
    height = models.CharField(max_length=25)
    width = models.CharField(max_length=25)
    weight = models.CharField(max_length=25)
    islong = models.CharField(max_length=25)
    passengers = models.CharField(max_length=25)
    stage1 = models.BooleanField(default=False)
    price = models.CharField(max_length=25)
    stage2 = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
