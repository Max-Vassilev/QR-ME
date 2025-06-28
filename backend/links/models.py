from django.db import models
from django.conf import settings

class Link(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="links")
    platform = models.CharField(max_length=50)
    url = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform
