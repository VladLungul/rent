# Generated by Django 2.1.3 on 2018-12-15 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20181214_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='images',
        ),
        migrations.AddField(
            model_name='carimage',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
            preserve_default=False,
        ),
    ]
