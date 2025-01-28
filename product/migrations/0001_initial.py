# Generated by Django 5.1.5 on 2025-01-26 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Product Price')),
                ('stock_quantity', models.PositiveBigIntegerField(default=1, verbose_name='Product Quantity')),
                ('status', models.CharField(choices=[('available', 'Availble'), ('not_available', 'Not Avaiable')], default='available', max_length=60, verbose_name='Status')),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Category')),
            ],
        ),
    ]
