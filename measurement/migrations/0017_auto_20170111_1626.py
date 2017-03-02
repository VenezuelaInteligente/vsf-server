# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-11 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0016_auto_20161206_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='manual_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='flag',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='isp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
