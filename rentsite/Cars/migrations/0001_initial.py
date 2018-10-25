# Generated by Django 2.1.2 on 2018-10-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('grade', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=4)),
                ('vin', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Бензин'), ('Diesel', 'Дизель'), ('Gas/Petrol', 'Газ/бензин'), ('Hybrid', 'Гибрид')], max_length=25)),
                ('engine_capacity', models.CharField(max_length=20)),
                ('drive_unit', models.CharField(max_length=20)),
                ('gearbox', models.CharField(max_length=20)),
                ('car_class', models.CharField(max_length=20)),
                ('rent_type', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('discount', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=25)),
                ('photos', models.ImageField(upload_to='')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
