from django.db import models
from cars.choice import RENT_TYPE

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    user_id = models.CharField(max_length=25)
    user_phonenumber = models.CharField(max_length=25)
    car_id = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    starttime = models.DateTimeField()
    finishtime = models.DateTimeField()
    city = models.CharField(max_length=25)
    owner_id = models.CharField(max_length=25)
    rent_type = models.CharField(choices=RENT_TYPE, max_length=25)
    discount = models.CharField(max_length=25)

