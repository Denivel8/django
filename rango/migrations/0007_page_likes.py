# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20180122_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
