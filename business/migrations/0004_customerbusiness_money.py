# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-22 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20200918_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerbusiness',
            name='money',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='预估金额'),
        ),
    ]
