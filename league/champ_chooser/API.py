
import requests
from django.conf import settings
from .serializers import SummonerSpellSerializer
import regex as re


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


def get_summoner_spells_all(region, locale):
    url = "https://{region}.api.riotgames.com/lol/static-data/v3/summoner-spells?locale={locale}&dataById=false".format(region=region, locale=locale)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()

    return json


def get_summoner_league(region, summoner_id):  # cass version of this not implemented
    url = "https://{region}.api.riotgames.com/lol/league/v3/positions/by-summoner/{summoner_id}".format(region=region, summoner_id=summoner_id)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()

    return json


def update_summoner_spell_info():
    data = get_summoner_spells_all('na1', 'en_US')

    for d in data['data']:
        s = SummonerSpellSerializer(data=data['data'][d])
        if s.is_valid():
            s.save()


def validate_summoner_name(name):

    name_regex = re.compile(u'^[0-9\\p{L} _\\.]+$')
    validated_name = re.search(name_regex, name)

    if validated_name:
        return validated_name[0]
    else:
        return None


