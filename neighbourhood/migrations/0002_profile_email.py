# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-23 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
