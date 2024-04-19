from django.db import models
from django.contrib.auth.models import Permission

class CustomUserPermission(models.Model):
    user = models.ForeignKey('searchapp.CustomUser', on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
