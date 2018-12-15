from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    city = models.CharField(max_length=25, default="Киев")
    owner_type = models.CharField(
        max_length=25,
        choices=(
            ('Private', 'Частное лицо'),
            ('Company', 'Организация')),
        default='Private'
    )
    photo = models.ImageField(upload_to="photos", default="photos/default.png")
