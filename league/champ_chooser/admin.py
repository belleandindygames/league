# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Summoner_V3

# Register your models here.
#admin.site.register(Summoner_V3)

@admin.register(Summoner_V3)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'summonerLevel', 'profileIconId', 'id', 'accountId', 'revisionDate')

