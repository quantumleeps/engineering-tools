# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_remove_pumpspecification_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='pumpspecification',
            name='doc_num',
            field=models.IntegerField(default=1),
        ),
    ]
