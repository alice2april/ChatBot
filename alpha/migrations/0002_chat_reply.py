# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='reply',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
