# Generated by Django 3.2 on 2021-05-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_prdalt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prd_alternative',
            name='PRDAlternative',
        ),
        migrations.RemoveField(
            model_name='prd_alternative',
            name='PRDSlc',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDACSS',
            field=models.ManyToManyField(related_name='_product_product_PRDACSS_+', to='product.product', verbose_name='Accessories'),
        ),
        migrations.DeleteModel(
            name='PRD_Accessory',
        ),
        migrations.DeleteModel(
            name='PRD_Alternative',
        ),
    ]
