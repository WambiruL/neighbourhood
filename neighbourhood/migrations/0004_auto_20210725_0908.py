# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-25 09:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhood', '0003_auto_20210723_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='occupants',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
