from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    grade = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    vin = models.CharField(max_length=20)
    fuel_type = models.CharField(choises=(
        ('Petrol','Бензин'),
        ('Diesel','Дизель'),
        ('Gas/Petrol','Газ/бензин'),
        ('Hybrid', 'Гибрид') )
    engine_capacity = models.CharField(max_length=20)
    drive_unit = models.CharField(max_length=20)
    gearbox = models.CharField(max_length=20)
    car_class = models.CharField(max_length=20)
    rent_type = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False,auto_now=True)
    owner = models.CharField(max_length=25)
    photos = models.ImageField()
    city = models.CharField(max_length=20)

    @property
    def __str__(self):
        return f'S({self.car_id}, {self.manufacturer},{self.model}, {self.grade}, {self.year},
        {self.vin}, {self.fuel_type},{self.engine_capacity}, {self.drive_unit}, {self.gearbox},
        {self.car_class}, {self.rent_type},{self.price}, {self.discount}, {self.active},
        {self.car_id}, {self.manufacturer}, {self.model}, {self.grade}, {self.year}
        )'

    def __repr__(self):
        return self.__str__






