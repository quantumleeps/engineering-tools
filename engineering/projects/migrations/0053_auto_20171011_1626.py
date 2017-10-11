# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0052_controlleddocument_historicalcontrolleddocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlleddocument',
            name='system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.System'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controlleddocument',
            name='system_drawing_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalcontrolleddocument',
            name='system',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.System'),
        ),
        migrations.AddField(
            model_name='historicalcontrolleddocument',
            name='system_drawing_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='controlleddocument',
            name='drawing_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcontrolleddocument',
            name='drawing_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
