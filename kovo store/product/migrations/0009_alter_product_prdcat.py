# Generated by Django 3.2 on 2021-05-18 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210518_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDCat',
            field=models.ForeignKey(limit_choices_to={'PRDCat_Parent__isnull : False'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PRDCategory', to='product.prd_cat'),
        ),
    ]