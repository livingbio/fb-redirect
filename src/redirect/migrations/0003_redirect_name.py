# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0002_auto_20160120_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirect',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
