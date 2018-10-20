from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    user_type = models.CharField(max_length=25)
    user_id = models.CharField(max_length=25)
    user_phonenumber = models.CharField(max_length=25)
    car_id = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    owner_id = models.CharField(max_length=25)
    rent_type = models.CharField(max_length=25)
    discount = models.CharField(max_length=25)

