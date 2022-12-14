# Generated by Django 3.2 on 2021-05-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRDName', models.CharField(max_length=15, verbose_name='Brand name')),
                ('BRRDescription', models.TextField(blank=True, null=True, verbose_name='Brand description')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VRTName', models.CharField(max_length=15, verbose_name='Variant name')),
                ('VRTescription', models.TextField(blank=True, null=True, verbose_name='Variant description')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
    ]
