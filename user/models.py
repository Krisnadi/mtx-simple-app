from django.contrib.auth.models import User
from django.db import models


class UserMeta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_count = models.PositiveIntegerField(default=0)
    last_session = models.DateTimeField(null=True, blank=True)
