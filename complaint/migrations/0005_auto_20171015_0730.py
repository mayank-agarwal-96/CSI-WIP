# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0004_auto_20171014_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='department',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
