# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-03 12:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_de', models.CharField(max_length=100, null=True)),
                ('title_es', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_es', models.TextField(null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('draft', models.BooleanField(default=True)),
                ('twitter_search', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('display_name', models.CharField(max_length=50)),
                ('display_name_de', models.CharField(max_length=50, null=True)),
                ('display_name_es', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('title_de', models.CharField(max_length=100, null=True)),
                ('title_es', models.CharField(max_length=100, null=True)),
                ('text', models.TextField()),
                ('text_de', models.TextField(null=True)),
                ('text_es', models.TextField(null=True)),
                ('category', models.CharField(choices=[('info', 'Info'), ('grave', 'Grave'), ('positivo', 'Positivo')], max_length=20)),
                ('created', models.DateField(default=datetime.date.today)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='Case.Case')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='Case.Category'),
        ),
        migrations.AddField(
            model_name='case',
            name='events',
            field=models.ManyToManyField(related_name='cases', to='event.Event'),
        ),
    ]
