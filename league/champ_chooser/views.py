# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.shortcuts import render
from .forms import submit_summoner_info
from serializers import Summoner_V3_Serializer
from models import Summoner_V3
from datetime import datetime

# Create your views here.
def Get_Summoner_V3(request):

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
                    serializer = Summoner_V3_Serializer(data=json)

                    if serializer.is_valid():
                        summoner = serializer.save()
                        summoner.region = region
                        summoner.save()

                        print(summoner)

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

                if serializer.is_valid():
                    summoner = serializer.save()
                    summoner.region = region
                    summoner.save()

                    print(summoner)

                    return render(request, 'summoner_details.html', {'summoner': summoner})

                else:
                    print('no summoner by that name exists in this region')

    else:
        form = submit_summoner_info()



    return render(request, 'index.html', {'form': form})

