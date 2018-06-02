# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhawks', '0007_auto_20180526_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='slug',
            field=models.SlugField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='lostandfound',
            name='slug',
            field=models.SlugField(default=None, max_length=500),
        ),
    ]
