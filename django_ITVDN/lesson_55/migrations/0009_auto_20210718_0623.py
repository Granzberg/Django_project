# Generated by Django 3.1.13 on 2021-07-18 06:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_55', '0008_auto_20210717_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinternet',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('375e42b8-b672-4cfe-9c7e-a79743db5a2b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
