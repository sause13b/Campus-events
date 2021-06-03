from django.db import models


class FormOfEventInformation(models.Model):
    participation = models.BooleanField()

