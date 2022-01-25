# Generated by Django 3.2.9 on 2021-12-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0004_auto_20211115_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='spare',
            name='faults',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Faults'),
        ),
        migrations.AddField(
            model_name='spare',
            name='local_or_global',
            field=models.BooleanField(default=False, verbose_name='Warranty in Egypt ?'),
        ),
    ]