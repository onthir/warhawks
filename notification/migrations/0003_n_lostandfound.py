# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 12:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warhawks', '0012_auto_20180607_1815'),
        ('notification', '0002_auto_20180607_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='N_lostandfound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=100)),
                ('read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_lost', to=settings.AUTH_USER_MODEL)),
                ('lf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.LostAndFound')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.LFComment')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_lost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
