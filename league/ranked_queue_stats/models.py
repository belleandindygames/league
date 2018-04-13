

"""

from django.db import models


# Create your models here.
class User(models.Model):
    summoner_name = models.Charfield(max_length=30)
    account_id = models.Charfield(max_length=30)
    time_stamp = models.Charfield(max_length=30)


class Gamelist(models.Model):
    account_id = models.IntegerField()
    platform_id = models.Charfield(max_length=30)
    game_id = models.BigIntegerField()
    champion = models.PositiveSmallIntegerField()
    queue = models.Charfield(max_length=30)
    season = models.SmallIntegerField()
    time_stamp = models.Charfield(max_length=30)
    role = models.Charfield(max_length=30)
    lane = models.Charfield(max_length=30)
    win = models.Charfield(max_length=30)
"""

