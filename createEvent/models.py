from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, null=True)
    info = models.TextField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    date = models.DateField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def create_event(self):
        self.save()



