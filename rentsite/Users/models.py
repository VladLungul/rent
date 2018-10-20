from django.db import models

class RegisteredUser(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=25)
    outcoming_orders = models.CharField(max_length=25)
    discount = models.CharField(max_length=25)
    city = models.CharField(max_length=25)



class UnregisteredUser(models.Model):
    name = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)





