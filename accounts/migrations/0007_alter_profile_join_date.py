# Generated by Django 3.2.9 on 2022-01-09 03:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 5, 28, 17, 358081), verbose_name='Join Date'),
        ),
    ]
