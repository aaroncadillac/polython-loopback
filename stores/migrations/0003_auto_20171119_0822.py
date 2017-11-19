# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='products',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[{'id': '6be25512-0400-4c44-bf95-656d487eed07', 'name': 'demo_product', 'price': 50, 'quantity': 5}]),
        ),
    ]
