from django.db import models

# Create your models here.
class PersonalAreaInformation(models.Model):
    login = models.TextField()
    date_of_birth = models.DateField()
    sex = models.TextField()
    corporate_email = models.TextField()
    personal_email = models.TextField()
    mobile_phone = models.TextField()