# Generated by Django 2.1.3 on 2018-12-18 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0002_auto_20181212_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
