# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0011_auto_20210726_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Your Email Address', max_length=200, null=True),
        ),
    ]
