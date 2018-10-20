from django.db import models

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    cash_account = models.CharField(max_length=25)
    discount = models.CharField(max_length=25)
    owner_type = models.CharField(max_length=25)
    own_cars = models.CharField(max_length=25)
    incoming_orders = models.CharField(max_length=25)
    city = models.CharField(max_length=25)







