# Generated by Django 3.2 on 2021-05-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_deal_dlimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='prd_img',
            name='PRDImg2',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Product Image 2'),
        ),
        migrations.AddField(
            model_name='prd_img',
            name='PRDImg3',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Product Image 3'),
        ),
        migrations.AlterField(
            model_name='prd_img',
            name='PRDImg',
            field=models.ImageField(upload_to='product/', verbose_name='Product Image 1'),
        ),
    ]
