# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20160305_1340'),
        ('my_social', '0003_groupparticipation_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date started')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Event')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_social.Group')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
