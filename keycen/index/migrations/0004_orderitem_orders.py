# Generated by Django 3.2 on 2021-12-23 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_guestcostumer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('delivred', models.BooleanField(default=False)),
                ('costumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.guestcostumer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Variant', models.CharField(blank=True, max_length=40, null=True)),
                ('AddAt', models.DateTimeField(auto_now_add=True)),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.orders')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.product')),
            ],
        ),
    ]