# Generated by Django 3.2 on 2021-05-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_intads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intads',
            name='INTADate',
            field=models.DateField(blank=True, null=True, verbose_name='Added at:'),
        ),
    ]