# Generated by Django 3.2 on 2021-05-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_prdalt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prd_img',
            name='PRDImg',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Product Image 1'),
        ),
    ]