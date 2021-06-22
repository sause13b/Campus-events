from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

    def __str__(self):
        return self.user.username


