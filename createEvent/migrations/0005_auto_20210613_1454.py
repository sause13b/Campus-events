# Generated by Django 3.2.4 on 2021-06-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createEvent', '0004_auto_20210613_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='vk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]