# Generated by Django 3.2 on 2021-05-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210515_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prd_cat',
            name='PRDCat_img',
            field=models.ImageField(blank=True, null=True, upload_to='categories', verbose_name='Categorie image'),
        ),
    ]