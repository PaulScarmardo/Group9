# Generated by Django 3.1.7 on 2023-04-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='userType',
            field=models.CharField(default='buyer', max_length=50),
            preserve_default=False,
        ),
    ]
