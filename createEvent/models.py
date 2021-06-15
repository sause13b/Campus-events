from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    members = models.CharField(max_length=4, null=True, blank=True)
    vk = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='author_set')
    members_list = models.ManyToManyField(User, null=True, blank=True, related_name='members_set')

    def __str__(self):
        return self.name



