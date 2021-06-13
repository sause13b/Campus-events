from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    members = models.CharField(max_length=4, null=True)
    vk = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    date = models.DateField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def create_event(self):
        self.save()



