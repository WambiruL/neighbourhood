# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0010_auto_20210726_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighbourhood.Neighbourhood'),
        ),
    ]
