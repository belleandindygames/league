# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summoner_V3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_icon_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=40)),
                ('summoner_level', models.IntegerField(default=0)),
                ('revision_date', models.IntegerField(default=0)),
                ('summoner_id', models.IntegerField(default=0)),
                ('account_id', models.IntegerField(default=0)),
            ],
        ),
    ]