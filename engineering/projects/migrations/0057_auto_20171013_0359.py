# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0056_auto_20171013_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltank',
            name='capacity_units',
            field=models.CharField(blank=True, default='US Gal', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tank',
            name='capacity_units',
            field=models.CharField(blank=True, default='US Gal', max_length=20, null=True),
        ),
    ]
