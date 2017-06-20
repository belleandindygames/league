# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

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
            num_results = Summoner_V3.objects.filter(name__iexact=name).count()
            print(name)
            print(num_results)
            if num_results == 1:
                print('record exists')
                summoner = Summoner_V3.objects.get(name__iexact=name)
                print(summoner.name)
                return render(request, 'summoner_details.html', {'summoner': summoner})
            else:
                # lookup name in db before doing get request if found render oage with correct data

                region = form.cleaned_data['region']
                url = 'https://' + region +'.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name
                headers = { 'X-Riot-Token': settings.RIOT_API_KEY }
                r = requests.get(url, headers=headers)
                json = r.json()
                print(json['accountId'])
                serializer = Summoner_V3_Serializer(data=json)
                if serializer.is_valid():
                    summoner = serializer.save()
                    print(summoner)
                    return render(request, 'summoner_details.html', { 'summoner': summoner, 'json': json})

    else:
        form = submit_summoner_info()



    return render(request, 'index.html', {'form': form})

