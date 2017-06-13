from rest_framework import serializers
from .models import Summoner_V3

class Summoner_V3_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Summoner_V3

        fields = '__all__'