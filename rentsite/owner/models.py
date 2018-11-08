from django.db import models


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    cash_account = models.CharField(max_length=25, default=0)
    registration_photo = models.ImageField()
    ident_code = models.CharField(max_length=14)
    owner_type = models.CharField(max_length=25, choices=(('Private', 'Частное лицо'), ('Company', 'Организация')))
    own_cars = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='+',)
    incoming_orders = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f'S({self.owner_id}, {self.name},{self.phonenumber}, {self.email}, {self.password},' \
               f'{self.cash_account}, {self.registration_photo},{self.owner_type}, {self.incoming_orders},' \
               f'{self.city}, {self.own_cars}, {self.ident_code}, {self.approve})'

    def __repr__(self):
        return self.__str__


class BlackList(models.Model):
    blackownerid = models.ForeignKey(Owner, related_name='owneridblack', on_delete=models.CASCADE)
    owner_phonenumber = models.CharField(max_length=25, default=0)
    carsinblacklistvin = models.TextField()



    def __str__(self):
        return f'S({self.blackownerid}, {self.owner_phonenumber}, {self.carsinblacklistvin})'

    def __repr__(self):
        return self.__str__