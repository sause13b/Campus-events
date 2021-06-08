# Generated by Django 3.2.3 on 2021-06-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('info', models.TextField(null=True)),
                ('category', models.CharField(choices=[('Официальный', 'Официальный'), ('Неофициальный', 'Нефициальный')], max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('members', models.CharField(max_length=3, null=True)),
                ('vk', models.CharField(max_length=200, null=True)),
                ('mail', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
