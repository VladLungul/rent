from django.db import models

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    cash_account = models.CharField(max_length=25, default=0)
    discount = models.CharField(max_length=25)
    owner_type = models.CharField(max_length=25, choices=(('Private', 'Частное лицо'), ('Company', 'Организация')))
    own_cars = models.CharField(max_length=25)
    incoming_orders = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

    def __str__(self):
        return f'S({self.owner_id}, {self.name},{self.phonenumber}, {self.email}, {self.password},' \
               f'{self.cash_account}, {self.discount},{self.owner_type}, {self.own_cars}, {self.incoming_orders},' \
               f'{self.city})'

    def __repr__(self):
        return self.__str__

