# Generated by Django 3.1.7 on 2023-04-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
