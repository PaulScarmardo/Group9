# Generated by Django 3.1.7 on 2023-04-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]