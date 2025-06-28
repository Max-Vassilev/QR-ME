from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
