# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20171009_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pumpop',
            name='pump',
        ),
        migrations.RemoveField(
            model_name='pumppart',
            name='pump',
        ),
        migrations.DeleteModel(
            name='PumpOP',
        ),
        migrations.DeleteModel(
            name='PumpPart',
        ),
    ]