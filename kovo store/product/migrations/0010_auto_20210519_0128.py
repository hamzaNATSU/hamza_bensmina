# Generated by Django 3.2 on 2021-05-19 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_prdcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DLName', models.CharField(max_length=20, verbose_name='Deal title')),
                ('DLimg', models.ImageField(upload_to='Deals/', verbose_name='Deal image')),
                ('DLDesc', models.TextField(max_length=40, verbose_name='Deal description')),
            ],
            options={
                'verbose_name': 'Deal',
                'verbose_name_plural': 'Deals',
            },
        ),
        migrations.AlterField(
            model_name='prd_cat',
            name='PRDCat_Parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'PRDCat_Parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.prd_cat', verbose_name='main category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCat',
            field=models.ForeignKey(limit_choices_to={'PRDCat_Parent__isnull': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PRDCategory', to='product.prd_cat'),
        ),
    ]