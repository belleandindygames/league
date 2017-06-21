from rest_framework import serializers
from .models import Summoner_V3


class Summoner_V3_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Summoner_V3

        fields = '__all__'


class LiveMatchSerializer(serializers.Serializer):

    gameId = serializers.IntegerField()
    gameStartTime = serializers.IntegerField()
    gameMode = serializers.CharField()

    def create(self, validated_data):
        return LiveMatch(**validated_data)


class LiveMatch(object):
    def __init__(self, gameId, gameStartTime, gameMode):
        self.gameId = gameId
        self.gameStartTime = gameStartTime
        self.gameMode = gameMode

