# Generated by Django 4.0.3 on 2022-09-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0025_alter_catiegorys_id_alter_favorite_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
