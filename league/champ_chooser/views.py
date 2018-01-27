# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Std lib imports
import logging
import os

# Django imports
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# App imports
from .forms import submit_summoner_info
from .serializers import Summoner_V3_Serializer, LiveMatchSerializer, ChampionInfoSerializer
from .models import Summoner_V3, Champion
from .data import platform
from .API import get_live_match, validate_summoner_name, get_basic_champ_info, update_summoner_spell_info

# 3rd party imports
import requests

# Cass
import cassiopeia as cass
from cassiopeia.core import Summoner


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
                if summoner.region == platform(region):

                    return render(request, 'summoner_details.html', {'summoner': summoner})

                else:
                    # lookup name in db before doing get request if found render oage with correct data
                    url = 'https://' + platform(region) + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
                    headers = {'X-Riot-Token': settings.RIOT_API_KEY}
                    r = requests.get(url, headers=headers)
                    json = r.json()
                    print('JSON RESPONSE')
                    print(json.id)
                    serializer = Summoner_V3_Serializer(data=json)

                    if serializer.is_valid():
                        summoner = serializer.save()
                        summoner.region = platform(region)
                        summoner.save()

                        return render(request, 'summoner_details.html', {'summoner': summoner})

                    else:
                        print('no summoner by that name exists in this region')

            else:
                # lookup name in db before doing get request if found render oage with correct data
                url = 'https://' + platform(region) + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
                headers = { 'X-Riot-Token': settings.RIOT_API_KEY }
                r = requests.get(url, headers=headers)
                json = r.json()
                serializer = Summoner_V3_Serializer(data=json)
                print(json)
                if serializer.is_valid():
                    summoner = serializer.save()
                    summoner.region = platform(region)
                    summoner.save()

                    return render(request, 'summoner_details.html', {'summoner': summoner})

                else:
                    print('no summoner by that name exists in this region')

    else:
        form = submit_summoner_info()

    return render(request, 'summoner.html', {'form': form})


def summoner_wrapper(name, region):
    stripped_name = name.replace(" ", "")
    return Summoner(name=stripped_name, region=region)


##############
# LIVE MATCH #
##############


def live_match(request):

    if request.method == "POST":
        form = submit_summoner_info(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            region = form.cleaned_data['region']

            summoner = validate_summoner_name(name)   # summoner_wrapper(name=name, region=region)
            summoner = summoner.replace(" ", "")
            if summoner:
                # get match data
                print('summoner is valid')
                region = region.lower()
                return redirect('{}/{}/'.format(region, summoner))
    else:
        form = submit_summoner_info()

    return render(request, 'live_match.html', {'form': form})


def live_match_detail(request, region, summoner_name):

    region = region.upper()
    summoner = summoner_wrapper(name=summoner_name, region=region)

    if summoner:
        # TODO: rewrite to prep data for template and don't use of custom  tags
        
        match_data = get_live_match(summoner.id, platform(region))
        match_serialized = LiveMatchSerializer(data=match_data)

        if match_serialized.is_valid():
            match = match_serialized.save()
            patch = settings.CURRENT_PATCH
            print(patch)
            return render(request, 'live_match_details.html', {'match': match, 'patch': patch})
        else:
            print("Summoner not in game")
            # get all champions/summoners --DONE

            # get summoner stats

            # get summoner masteries
            return render(request, 'summoner_not_in_game.html')
    else:
        print('Summoner does not exist')
        # replace this with summoner does not exist page
        return render(request, 'summoner_noexist.html', {'name': summoner, 'region': region})


class ApiLiveMatch(APIView):

    def get(self, request, region, summoner_name):
        region = region.upper()
        summoner = summoner_wrapper(name=summoner_name, region=region)

        if summoner:
            match_data = get_live_match(summoner.id, platform(region))
            match_serialized = LiveMatchSerializer(data=match_data)

            if match_serialized.is_valid():
                match = match_serialized.save()
                patch = settings.CURRENT_PATCH
                
                return Response(match_data)
            else:
                # return json with summoner in game
                return None

        else:
            # return json with summoner does not exist
            return None 


class ChampionInfoView(APIView):

    def get(self, request):
        champions = Champion.objects.all()
        serializer = ChampionInfoSerializer(champions, many=True)
        return Response(serializer.data)

    '''
    def update(self, request):
        champs = cass.get_champions()
        for champ in champs:
            champion = Champion(
                id=champ.id,
                name=champ.name,
                key=champ.key
            ).save()

        return HttpResponse("OK")
    '''

        

##############
#    TEST    #
##############


def test_something(request):

    result = 0
    return render(request, 'test.html',  {'result': result})


##############
#    TEST    #
##############


class FrontendAppView(View):
    """
    Serves react app
    """
    def get(self, request):
        try:
            with open(os.path.join(str(settings.REACT_APP_DIR), 'build', 'index.html')) as f:

                return HttpResponse(f.read())

        except FileNotFoundError:
            logging.exception('App build not found')
            return HttpResponse(
            """
            This URL for prod only, Use http://localhost:3000/ (yarn run start) in development 
            or (yarn run build) for generate the production bundle.
            """,
                status=501,
            )

