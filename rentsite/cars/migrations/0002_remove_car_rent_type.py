# Generated by Django 2.1.3 on 2018-12-14 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rent_type',
        ),
    ]
