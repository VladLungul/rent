# Generated by Django 2.1.2 on 2018-11-02 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0005_auto_20181102_1514'),
        ('owner', '0003_remove_owner_own_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='own_cars',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
            preserve_default=False,
        ),
    ]