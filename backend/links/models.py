from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")
    platform = models.CharField(max_length=50)
    url = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label or self.platform
