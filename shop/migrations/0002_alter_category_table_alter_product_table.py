# Generated by Django 5.0.6 on 2024-12-05 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]
