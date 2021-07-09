# Generated by Django 3.2.4 on 2021-07-07 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_55', '0004_alter_clientinternet_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinternet',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('837d582b-224d-4153-a10b-b64aa09ff1dd'), editable=False, primary_key=True, serialize=False),
        ),
    ]