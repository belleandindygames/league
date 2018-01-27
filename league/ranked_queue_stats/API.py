import requests
import time

RIOT_API_KEY = 'RGAPI-61f9aa6d-0e09-4d8c-bdca-3370ffce7919'
region = 'NA1'


# lazy and inefficient way to make sure that i stay within the rate call limits
def rest():
    time.sleep(1.2)


# gets a summoners information
def get_summoner_info(name, region):
    url = "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{name}".format(region=region, name=name)
    headers = {'X-Riot-Token': RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    rest()
    return json


# pull the most recent 20 games for a summoner
def get_summoner_recent_matchlist(region, accountId):
    url = "https://{region}.api.riotgames.com/lol/match/v3/matchlists/by-account/{accountId}/recent".format(region=region, accountId=accountId)
    headers = {'X-Riot-Token': RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    rest()
    return json


# pull the matchlist for a summoner
def get_summoner_matchlist(region, accountId):
    url = "https://{region}.api.riotgames.com/lol/match/v3/matchlists/by-account/{accountId}".format(region=region, accountId=accountId)
    headers = {'X-Riot-Token': RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    rest()
    return json


def get_summoner_matchlist_index(region, accountId, beginIndex):
    url = "https://{region}.api.riotgames.com/lol/match/v3/matchlists/by-account/{accountId}?beginIndex={beginIndex}".format(region=region, accountId=accountId, beginIndex=beginIndex)
    headers = {'X-Riot-Token': RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    rest()
    return json


# function to pull information about whether a summoner won a specific match
def get_summoner_matchinfo(matchId, region):
    url = "https://{region}.api.riotgames.com/lol/match/v3/matches/{matchId}".format(region=region, matchId=matchId)
    headers = {'X-Riot-Token': RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(url)
    rest()
    return json
