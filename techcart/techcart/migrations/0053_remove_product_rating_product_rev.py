# Generated by Django 4.0.6 on 2023-01-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0052_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='rev',
            field=models.IntegerField(null=True),
        ),
    ]
