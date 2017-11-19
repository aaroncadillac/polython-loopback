# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:29
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20171119_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='products',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[{'id': '1103e70b-1986-4414-a02d-ebd385c19f60', 'name': 'demo_product', 'price': 50, 'quantity': 5}], null=True),
        ),
    ]
