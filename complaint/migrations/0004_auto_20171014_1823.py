# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-14 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_profile_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]