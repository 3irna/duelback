# Generated by Django 5.1.2 on 2024-11-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0014_takereferralsprofithistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/', verbose_name='avatar'),
        ),
    ]
