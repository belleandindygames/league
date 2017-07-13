# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.shortcuts import render
from .forms import submit_summoner_info
from .serializers import Summoner_V3_Serializer, LiveMatchSerializer
from .models import Summoner_V3

from .data import platform
from .API import get_summoner_info, get_live_match, get_summoner_spell_info, update_summoner_spell_info, get_summoner_league

# Cass

import cassiopeia as cass
from cassiopeia.core import Summoner


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
                url = 'https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
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


def summoner_wrapper(name, region):
    stripped_name = name.replace(" ", "")
    return Summoner(name=stripped_name, region=region)


def live_match(request):

    if request.method == "POST":
        form = submit_summoner_info(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            region = form.cleaned_data['region']
            summoner = summoner_wrapper(name=name, region=region)

            if summoner:
                # get match data
                match_data = get_live_match(summoner.id, platform(region))
                match_serialized = LiveMatchSerializer(data=match_data)

                if match_serialized.is_valid():
                    match = match_serialized.save()
                    patch = settings.CURRENT_PATCH
                    print(patch)
                    return render(request, 'live_match_details.html', {'match': match, 'patch': patch})
                else:
                    print("invalid data")
                # get all champions/summoners --DONE

                # get summoner stats

                # get summoner masteries

    else:
        form = submit_summoner_info()

    return render(request, 'live_match.html', {'form': form})


def test_something(request):

    result = 0
    return render(request, 'test.html',  {'result': result})



