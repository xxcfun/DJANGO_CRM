# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-12 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrecord',
            name='next',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='后期规划'),
        ),
    ]
