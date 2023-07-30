# Generated by Django 2.2 on 2022-09-21 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techcart', '0019_auto_20220920_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users',
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(null=True, to='techcart.product')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='orders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='techcart.order'),
        ),
    ]
