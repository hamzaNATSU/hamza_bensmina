# Generated by Django 3.2 on 2021-06-29 16:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20210623_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingadress',
            name='country',
            field=django_countries.fields.CountryField(default='morocco', max_length=2),
        ),
    ]