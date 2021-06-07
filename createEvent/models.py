from django.db import models


class Create(models.Model):
    CATEGORY = (
        ('Официальный', 'Официальный'),
        ('Неофициальный', 'Нефициальный'),
                )
    title = models.CharField(max_length=200, null=True)
    info = models.TextField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    address = models.CharField(max_length=200, null=True)
    members = models.CharField(max_length=3, null=True)
    vk = models.CharField(max_length=200, null=True)
    mail = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
