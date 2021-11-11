# Generated by Django 3.2.9 on 2021-11-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20211111_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('xiaomi', 'xiaomi'), ('Infinix', 'Infinix'), ('Nokia', 'Nokia'), ('Sony', 'Sony'), ('LG', 'LG'), ('HTC', 'HTC'), ('Lenovo', 'Lenovo'), ('Realme', 'Realme'), ('Honor', 'Honor'), ('ZTE', 'ZTE'), ('Vivo', 'Vivo'), ('Alcatel', 'Alcatel'), ('Asus', 'Asus'), ('Motorola', 'Motorola'), ('Acer', 'Acer'), ('Techno', 'Techno')], max_length=100, verbose_name='Brand Name'),
        ),
    ]
