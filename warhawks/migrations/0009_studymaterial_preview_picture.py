# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhawks', '0008_auto_20180529_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymaterial',
            name='preview_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
