# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinbaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sell', models.DecimalField(decimal_places=10, max_digits=20)),
                ('currency', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CoinhakoHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sell', models.DecimalField(decimal_places=10, max_digits=20)),
                ('currency', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LiveData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sell', models.DecimalField(decimal_places=10, max_digits=20)),
                ('buyFees', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sellFees', models.DecimalField(decimal_places=10, max_digits=20)),
                ('siteId', models.IntegerField()),
                ('currency', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ZebpayHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sell', models.DecimalField(decimal_places=10, max_digits=20)),
                ('currency', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]