# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champ_chooser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summoner_v3',
            old_name='account_id',
            new_name='accountId',
        ),
    ]
