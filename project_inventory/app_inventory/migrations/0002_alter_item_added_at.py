# Generated by Django 4.1.4 on 2022-12-16 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 35, 56, 846357)),
        ),
    ]
