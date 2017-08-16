# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20170816_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valve',
            name='detailedDescription',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='installtype',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='material',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='pipeflangeclass',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='pressure',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='temperature',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='valvemodel',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='valve',
            name='vendor',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
