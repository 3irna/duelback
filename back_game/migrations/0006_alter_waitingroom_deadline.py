# Generated by Django 5.1.2 on 2024-10-21 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_game', '0005_alter_waitingroom_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitingroom',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 21, 17, 16, 59, 506725, tzinfo=datetime.timezone.utc)),
        ),
    ]
