# Generated by Django 3.2.4 on 2021-07-09 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(blank=True, max_length=10)),
                ('birthday', models.DateField(blank=True, default=datetime.date(1980, 12, 30))),
                ('gender', models.CharField(choices=[('1', 'male'), ('2', 'female')], max_length=60)),
            ],
        ),
    ]
