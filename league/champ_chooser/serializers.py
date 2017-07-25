from rest_framework import serializers
from .models import Summoner_V3, SummonerSpell, Champion


class Summoner_V3_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Summoner_V3

        fields = '__all__'


class BannedChampionsSerializer(serializers.Serializer):

    pickTurn = serializers.IntegerField()
    championId = serializers.IntegerField()
    teamId = serializers.IntegerField()

    def create(self, validated_data):
        return BannedChampions(**validated_data)


class ObserverSerializer(serializers.Serializer):

    encryptionKey = serializers.CharField()

    def create(self, validated_data):
        return Observer(**validated_data)


class RuneSerializer(serializers.Serializer):

    count = serializers.IntegerField()
    runeId = serializers.IntegerField()

    def create(self, validated_data):
        return Rune(**validated_data)


class MasterySerialzier(serializers.Serializer):

    masteryId = serializers.IntegerField()
    rank = serializers.IntegerField()

    def create(self, validated_data):
        return Mastery(**validated_data)


class GameParticipantSerializer(serializers.Serializer):

    profileIconId = serializers.IntegerField()
    championId = serializers.IntegerField()
    summonerName = serializers.CharField()
    runes = RuneSerializer(many=True)
    bot = serializers.BooleanField()
    teamId = serializers.IntegerField()
    spell2Id = serializers.IntegerField()
    masteries = MasterySerialzier(many=True)
    spell1Id = serializers.IntegerField()
    summonerId = serializers.IntegerField()
    spell2 = '700'

    def create(self, validated_data):
        gp = GameParticipant(**validated_data)
        return gp


class LiveMatchSerializer(serializers.Serializer):

    gameId = serializers.IntegerField()
    gameStartTime = serializers.IntegerField()
    platformId = serializers.CharField()
    gameMode = serializers.CharField()
    mapId = serializers.CharField()
    gameType = serializers.CharField()
    bannedChampions = BannedChampionsSerializer(many=True)
    observers = ObserverSerializer()
    participants = GameParticipantSerializer(many=True)
    gameLength = serializers.IntegerField()
    gameQueueConfigId = serializers.IntegerField()

    def create(self, validated_data):
        return LiveMatch(**validated_data)


# Serialization Objects

class LiveMatch(object):
    def __init__(self, gameId, gameStartTime, platformId, gameMode, mapId, gameType, bannedChampions, observers, participants, gameLength, gameQueueConfigId):
        self.gameId = gameId
        self.gameStartTime = gameStartTime
        self.platformId = platformId
        self.gameMode = gameMode
        self.mapId = mapId
        self.gameType = gameType
        self.bannedChampions = bannedChampions
        self.observers = observers
        self.participants = participants
        self.gameLenght = gameLength
        self.gameQueueConfigId = gameQueueConfigId


class BannedChampions(object):
    def __init__(self, pickTurn, championId, teamId):
        self.pickTurn = pickTurn
        self.championId = championId
        self.teamId = teamId


class Observer(object):
    def __init__(self, encryptionKey):
        self.encryptionKey = encryptionKey


class GameParticipant(object):
    def __init__(self, profileIconId, championId, summonerName, runes, bot, teamId, spell2Id, materies, spell1Id, summonerId):
        self.profileIconId = profileIconId
        self.championId = championId
        self.summonerName = summonerName
        self.runes = runes
        self.bot = bot
        self.teamId = teamId
        self.spell2Id = spell2Id
        self.masteries = materies
        self.spell1Id = spell1Id
        self.summonerId = summonerId
        self._spell1 = None
        self._spell2 = None


class Rune(object):
    def __init__(self, count, runeId):
        self.count = count
        self.runeId = runeId


class Mastery(object):
    def __init__(self, masteryId, rank):
        self.masteryId = masteryId
        self.rank = rank


###################
# Summoner Spells #
###################

class SummonerSpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = SummonerSpell

        fields = '__all__'

###################
#    Champions    #
###################

class ChampionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Champion
        fields = ('id', 'name', 'key')