# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.shortcuts import render
from .forms import submit_summoner_info
from serializers import Summoner_V3_Serializer, LiveMatchSerializer
from models import Summoner_V3
from datetime import datetime

# Create your views here.


def get_summoner_v3(request):

    if request.method == "POST":
        form = submit_summoner_info(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            region = form.cleaned_data['region']
            summoner_exists = Summoner_V3.objects.filter(name__iexact=name).exists()

            if summoner_exists:
                summoner = get_object_or_404(Summoner_V3, name__iexact=name)
                if summoner.region == region:

                    return render(request, 'summoner_details.html', {'summoner': summoner})

                else:
                    # lookup name in db before doing get request if found render oage with correct data
                    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
                    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
                    r = requests.get(url, headers=headers)
                    json = r.json()
                    print(json.id)
                    serializer = Summoner_V3_Serializer(data=json)

                    if serializer.is_valid():
                        summoner = serializer.save()
                        summoner.region = region
                        summoner.save()

                        return render(request, 'summoner_details.html', {'summoner': summoner})

                    else:
                        print('no summoner by that name exists in this region')

            else:
                # lookup name in db before doing get request if found render oage with correct data
                url = 'https://' + region +'.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
                headers = { 'X-Riot-Token': settings.RIOT_API_KEY }
                r = requests.get(url, headers=headers)
                json = r.json()
                serializer = Summoner_V3_Serializer(data=json)
                print(json)
                if serializer.is_valid():
                    summoner = serializer.save()
                    summoner.region = region
                    summoner.save()

                    return render(request, 'summoner_details.html', {'summoner': summoner})

                else:
                    print('no summoner by that name exists in this region')

    else:
        form = submit_summoner_info()

    return render(request, 'index.html', {'form': form})


def get_summoner_info(name, region):
    url = "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{name}".format(region=region, name=name)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()

    return json


def get_live_match(summonerid, region):
    url = "https://{region}.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{summoner}".format(region=region, summoner=summonerid)
    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    json = r.json()
    print('getlivematch')

    return json


def live_match(request):

    if request.method == "POST":
        form = submit_summoner_info(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            region = form.cleaned_data['region']
            summoner = get_summoner_info(name, region)
            print(summoner['id'])
            print(summoner['name'])
            if summoner:
                # get match data
                match_data = get_live_match(summoner['id'], region)
                match_serialized = LiveMatchSerializer(data=match_data)

                if match_serialized.is_valid():
                    match = match_serialized.save()
                    return render(request, 'live_match_details.html', {'match': match})
                else:
                    print("invalid data")
                # get all champions/summoners

                # get summoner stats

                # get summoner masteries

    else:
        form = submit_summoner_info()

    return render(request, 'live_match.html', {'form': form})

