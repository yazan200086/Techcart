# Generated by Django 4.0.6 on 2023-01-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0045_remove_cart_delivery_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
