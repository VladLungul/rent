# Generated by Django 2.1.3 on 2018-12-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20181214_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carimage',
            old_name='images',
            new_name='image',
        ),
    ]