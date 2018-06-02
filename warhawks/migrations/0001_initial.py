# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 02:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='a_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('edit', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=500)),
                ('distance_from_university', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=1000)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('a_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.a_type')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=1500)),
                ('salary', models.FloatField()),
                ('hits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='job_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('edit', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=500)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='j_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhawks.job_category'),
        ),
        migrations.AddField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
