# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0006_auto_20170904_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectedpoint',
            name='point',
        ),
        migrations.AddField(
            model_name='collectedpoint',
            name='inrange',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='collectedpoint',
            name='run',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.Run'),
        ),
        migrations.AddField(
            model_name='collectedpoint',
            name='units',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='collectedpoint',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
