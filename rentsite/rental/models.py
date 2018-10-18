from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    grade = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    fuel_type =
    engine_capacity =
    drive_unit =
    gearbox =
    car_class =
    rent_type =
    price =
    discount =
    active = models.BooleanField(default=False)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    owner =



class Owner(models.Model):


class RegisteredUser(models.Model):


class UnregisteredUser(models.Model):


