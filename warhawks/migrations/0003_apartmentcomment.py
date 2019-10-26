# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 03:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warhawks', '0002_auto_20180523_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('edit', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=500)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.Apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]