# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-23 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160319_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
