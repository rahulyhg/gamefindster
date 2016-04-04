# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20160404_1802'),
        ('accounts', '0015_remove_userinfo_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.City'),
        ),
    ]
