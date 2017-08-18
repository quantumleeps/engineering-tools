# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20170818_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectSystem'),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectSystem'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectSystem'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectSystem'),
        ),
        migrations.AlterField(
            model_name='valve',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectSystem'),
        ),
    ]
