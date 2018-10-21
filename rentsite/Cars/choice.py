fuel = (('Petrol', 'Бензин'),
        ('Diesel', 'Дизель'),
        ('Gas/Petrol', 'Газ/бензин'),
        ('Hybrid', 'Гибрид'))

YEAR_CHOICES = []
for r in range(1980, 2019):
    YEAR_CHOICES.append((r,r))
