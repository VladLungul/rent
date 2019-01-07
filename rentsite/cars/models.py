from django.db import models
from .choice import FUEL, YEAR_CHOICES, GEARBOX, CAR_CLASS, DRIVE_UNIT, RENT_TYPE
from django.conf import settings


class RentType(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()

    def __str__(self):
        return f'S({self.name}, {self.slug})'


class CarImage(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/%Y/%m/%d/')


class Car(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    grade = models.CharField(max_length=25)
    year = models.IntegerField(choices=YEAR_CHOICES)
    vin = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=25, choices=FUEL)
    engine_capacity = models.CharField(max_length=4)
    drive_unit = models.CharField(max_length=20, choices=DRIVE_UNIT)
    gearbox = models.CharField(max_length=20, choices=GEARBOX)
    car_class = models.CharField(max_length=20, choices=CAR_CLASS)
    rent_type = models.CharField(max_length=50, choices=RENT_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=20)
    description = models.TextField(default="")

    def __str__(self):
        return self.vin
