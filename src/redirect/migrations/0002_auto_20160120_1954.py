# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='redirect',
            name='short',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='clicklog',
            name='url',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='redirect.Redirect'),
        ),
    ]
