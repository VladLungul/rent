from django.db import models
from .choice import FUEL, YEAR_CHOICES, GEARBOX, CAR_CLASS, DRIVE_UNIT
#from owner.models import Owner


class Rent_type(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()

    def __str__(self):
        return f'S({self.name}, {self.slug})'

    def __repr__(self):
        return self.__str__


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
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
    rent_type = models.ForeignKey(Rent_type, related_name='renttype', on_delete=False, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    car_owner = models.ForeignKey('owner.Owner', related_name='carslist', on_delete=False, default=0)
    photos = models.ImageField(upload_to='cars/%Y/%m/%d/', blank=True, )
    city = models.CharField(max_length=20)
    description = models.TextField(default=0)

    def __str__(self):
        return f'S({self.car_id}, {self.manufacturer},{self.model}, {self.grade}, {self.year}, ' \
               f'{self.vin}, {self.fuel_type},{self.engine_capacity}, {self.drive_unit}, {self.gearbox},' \
               f'{self.car_class}, {self.rent_type},{self.price}, {self.discount}, {self.active},' \
               f'{self.create_date}, {self.update_date}, {self.photos}, {self.city}, {self.owner},' \
               f'{self.description})'

    def __repr__(self):
        return self.__str__
