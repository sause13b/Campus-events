# Generated by Django 3.2.3 on 2021-06-16 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAreaInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)),
                ('corporate_email', models.TextField()),
                ('personal_email', models.TextField()),
                ('mobile_phone', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
