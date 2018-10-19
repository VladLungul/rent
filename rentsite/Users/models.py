from django.db import models

class RegisteredUser(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber =
    outcoming_orders =
    discount =
    city =



class UnregisteredUser(models.Model):
    name = models.CharField(max_length=25)
    phonenumber =





