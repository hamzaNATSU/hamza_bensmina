# Generated by Django 3.2 on 2021-07-04 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('product', '0028_alter_shippingadress_isdefault'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrdRvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.profile')),
            ],
        ),
    ]
