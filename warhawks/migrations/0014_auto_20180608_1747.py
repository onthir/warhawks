# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 12:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhawks', '0013_auto_20180607_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostandfound',
            name='found_or_lost_on',
            field=models.DateField(default=datetime.datetime(2018, 6, 8, 17, 47, 13, 470415)),
        ),
    ]