# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-15 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20161202_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='private_evidence',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='public_evidence',
            field=models.TextField(blank=True, null=True),
        ),
    ]
