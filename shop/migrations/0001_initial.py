# Generated by Django 5.0.6 on 2024-12-05 20:10

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('description', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=False, help_text='0-Show, 1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('vendor', models.CharField(blank=True, max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('description', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=False, help_text='0-Show, 1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-Show, 1-Trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
