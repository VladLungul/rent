FUEL = (('Petrol', 'Бензин'),
        ('Diesel', 'Дизель'),
        ('Gas/Petrol', 'Газ/бензин'),
        ('Hybrid', 'Гибрид'))

YEAR_CHOICES = []
for r in range(1980, 2019):
    YEAR_CHOICES.append((r,r))


GEARBOX = (('Manual','Ручная'),
           ('Automatic', 'Автомат'))

CAR_CLASS = (('Econom', 'Эконом'),
             ('Middle', 'Средний'),
             ('Business', 'Бизнес'),
             ('Premium', 'Премиум'),
             ('Minivan', 'Минивэн'),
             ('Offroad', 'Внедорожник'),
             ('Electrocar', 'Электрокар'))

RENT_TYPE = (('Hourly', 'Почасовая аренда'),
             ('Daily', 'Посуточная аренда'),
             ('Long_term', 'Долгосрочная'),
             ('Transfer', 'Трансфер'),
             ('Bus_rent', 'Аренда автобуса'),
             ('Carwithdriver', 'Аренда авто с водителем'))

DRIVE_UNIT = (('RWD', 'Передний'),
              ('FWD', 'Задний'),
              ('AWD', 'Полный'))
