# Generated by Django 2.1.2 on 2018-11-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('owner', '0004_owner_own_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='own_cars',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
