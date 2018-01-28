from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Summoner_V3, SummonerSpell, Champion

# Register your models here.
# admin.site.register(Summoner_V3)


@admin.register(Summoner_V3)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'summonerLevel', 'profileIconId', 'id', 'accountId', 'revisionDate')


@admin.register(SummonerSpell)
class SummonerSpellsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'id')

