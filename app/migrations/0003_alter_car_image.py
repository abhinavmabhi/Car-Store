# Generated by Django 5.1.4 on 2025-04-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='car_image'),
        ),
    ]
