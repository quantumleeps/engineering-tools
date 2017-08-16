# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170816_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valve',
            name='pipeclass',
        ),
        migrations.AddField(
            model_name='valve',
            name='installtype',
            field=models.CharField(default='e.g., Flanged', max_length=40),
        ),
        migrations.AddField(
            model_name='valve',
            name='pipeflangeclass',
            field=models.CharField(default='e.g. 150#', max_length=40),
        ),
        migrations.AlterField(
            model_name='valve',
            name='detailedDescription',
            field=models.CharField(default='e.g. This valve isolates ER concentrate', max_length=255),
        ),
        migrations.AlterField(
            model_name='valve',
            name='material',
            field=models.CharField(default='e.g. PVC with EPDM', max_length=40),
        ),
        migrations.AlterField(
            model_name='valve',
            name='valvemodel',
            field=models.CharField(default='e.g. Type 57', max_length=40),
        ),
        migrations.AlterField(
            model_name='valve',
            name='vendor',
            field=models.CharField(default='e.g. Asahi', max_length=40),
        ),
    ]
