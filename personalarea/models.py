from django.db import models

# Create your models here.
class PersonalAreaInformation(models.Model):
    sex_choice = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    login = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=sex_choice)
    corporate_email = models.TextField()
    personal_email = models.TextField()
    mobile_phone = models.TextField()