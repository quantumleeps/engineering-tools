# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_auto_20171013_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinstrument',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
    ]
