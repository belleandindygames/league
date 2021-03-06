# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=20)),
                ('key', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Summoner_V3',
            fields=[
                ('profileIconId', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=40)),
                ('summonerLevel', models.IntegerField(default=0)),
                ('revisionDate', models.IntegerField(default=0)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('accountId', models.IntegerField(default=0)),
                ('region', models.CharField(default='NA1', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SummonerSpell',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('summonerLevel', models.IntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=50)),
                ('key', models.CharField(default=None, max_length=60)),
                ('description', models.CharField(default=None, max_length=500)),
            ],
        ),
    ]
