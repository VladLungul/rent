# Generated by Django 2.1.3 on 2018-11-28 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('grade', models.CharField(max_length=25)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)])),
                ('vin', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Бензин'), ('Diesel', 'Дизель'), ('Gas/Petrol', 'Газ/бензин'), ('Hybrid', 'Гибрид')], max_length=25)),
                ('engine_capacity', models.CharField(max_length=4)),
                ('drive_unit', models.CharField(choices=[('RWD', 'Передний'), ('FWD', 'Задний'), ('AWD', 'Полный')], max_length=20)),
                ('gearbox', models.CharField(choices=[('Manual', 'Ручная'), ('Automatic', 'Автомат')], max_length=20)),
                ('car_class', models.CharField(choices=[('Econom', 'Эконом'), ('Middle', 'Средний'), ('Business', 'Бизнес'), ('Premium', 'Премиум'), ('Minivan', 'Минивэн'), ('Offroad', 'Внедорожник'), ('Electrocar', 'Электрокар')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photos', models.ImageField(upload_to='cars/%Y/%m/%d/')),
                ('city', models.CharField(max_length=20)),
                ('description', models.TextField(default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rent_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='rent_type',
            field=models.ForeignKey(default=0, on_delete=False, to='cars.Rent_type'),
        ),
    ]
