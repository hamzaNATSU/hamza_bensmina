# Generated by Django 3.2 on 2022-02-24 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220222_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='DateRes',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 24, 16, 4, 18, 89951)),
        ),
    ]
