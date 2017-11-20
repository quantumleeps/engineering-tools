# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_auto_20171120_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvalve',
            name='ready_for_quote',
        ),
        migrations.RemoveField(
            model_name='valve',
            name='ready_for_quote',
        ),
        migrations.AlterField(
            model_name='historicalvalve',
            name='procurement_status',
            field=models.CharField(choices=[('sp', 'Specification Underway'), ('rq', 'Ready For Quote'), ('qo', 'Quote Requested'), ('qi', 'Received Quote'), ('op', 'Order Placed'), ('rc', 'Received by Engineering')], default='sp', max_length=2),
        ),
        migrations.AlterField(
            model_name='valve',
            name='procurement_status',
            field=models.CharField(choices=[('sp', 'Specification Underway'), ('rq', 'Ready For Quote'), ('qo', 'Quote Requested'), ('qi', 'Received Quote'), ('op', 'Order Placed'), ('rc', 'Received by Engineering')], default='sp', max_length=2),
        ),
    ]
