# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Summoner_V3(models.Model):
    profileIconId = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    summonerLevel = models.IntegerField(default=0)
    revisionDate = models.IntegerField(default=datetime.now)
    id = models.IntegerField(primary_key=True)
    accountId = models.IntegerField(default=0)

