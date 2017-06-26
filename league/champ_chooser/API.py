
import requests
from django.conf import settings


def get_summoner_info(name, region):
    url = "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{name}".format(region=region, name=name)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    return json


def get_live_match(summonerid, region):
    url = "https://{region}.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{summoner}".format(region=region, summoner=summonerid)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print('getlivematch')

    return json


def get_summoner_spell_info(region, spell, locale):
    url = "https://{region}.api.riotgames.com/lol/static-data/v3/summoner-spells/{id}?locale={locale}".format(region=region, id=spell, locale=locale)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()

    return json
