# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admprofapps', '0002_auto_20170117_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='screen_name',
            field=models.CharField(max_length=25),
        ),
    ]
