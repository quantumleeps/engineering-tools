# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20170816_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valve',
            name='service',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
