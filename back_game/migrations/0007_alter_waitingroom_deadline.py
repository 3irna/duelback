# Generated by Django 5.1.2 on 2024-10-21 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_game', '0006_alter_waitingroom_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitingroom',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 21, 17, 19, 14, 206257, tzinfo=datetime.timezone.utc)),
        ),
    ]