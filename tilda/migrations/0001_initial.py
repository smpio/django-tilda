# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TildaPage',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Page id')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('html', models.TextField(blank=True, verbose_name='HTML')),
                ('images', models.TextField(blank=True, verbose_name='Images')),
                ('css', models.TextField(blank=True, verbose_name='CSS')),
                ('js', models.TextField(blank=True, verbose_name='JS')),
                ('synchronized', models.DateTimeField(blank=True, null=True, verbose_name='Synchronized time')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'Tilda Pages',
                'ordering': ('title',),
            },
        ),
    ]
