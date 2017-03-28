# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-28 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_merge_20170320_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='dns',
            name='isp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.ISP', verbose_name='Operadora'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='input',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='metric',
            name='test_name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='plan',
            name='isp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.ISP'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='isp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.ISP'),
        ),
    ]
