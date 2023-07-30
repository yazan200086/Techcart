# Generated by Django 2.2 on 2022-09-14 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0011_auto_20220914_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorite_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='techcart.reviews'),
        ),
    ]
