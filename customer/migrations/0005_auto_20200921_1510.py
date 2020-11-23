# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-21 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200912_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='客户网址'),
        ),
    ]
