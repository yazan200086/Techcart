# Generated by Django 4.0.6 on 2023-01-19 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0041_remove_product_favorite_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='techcart.cart'),
        ),
    ]
