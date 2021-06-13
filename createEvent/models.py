from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    members = models.CharField(max_length=4, null=True, blank=True)
    vk = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.name

    def create_event(self):
        self.save()



