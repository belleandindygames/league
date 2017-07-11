from django import template
from ..API import get_summoner_spell_info, get_summoner_league
from ..models import SummonerSpell
from django.shortcuts import get_object_or_404
from cassiopeia.core import Champion
from ..data import game_q_config_id_to_name as game_id_to_name

register = template.Library()


@register.filter
def sum_spell_name(spell_id):
    try:
        spell = get_object_or_404(SummonerSpell, id=spell_id)
    except ValueError:
        return None
    return spell.key


@register.filter
def champ_name(champ_id):
    try:

        champ = Champion(id=champ_id)
    except ValueError:
        return None
    print(champ.name)
    return champ.key


@register.filter
def team_name(team):
    try:

        teams = {
            100: 'Blue',
            200: 'Red'
        }

        player_team = teams[team]
    except ValueError:
        return None

    return player_team


@register.filter
def banned_champ_blue(champions, index):
    cid = champions[index]['championId']
    if cid < 0:
        return None
    else:
        champ = Champion(id=cid)
        return champ.key


@register.filter
def banned_champ_red(champions, index):
    cid = champions[index+5]['championId']
    if cid < 0:
        return None
    else:
        champ = Champion(id=cid)
        return champ.key


@register.filter
def summoner_record(summoner_id, match):
    total = 0
    win_percent = 0

    try:
        region = match.platformId

        queue_type = game_id_to_name(match.gameQueueConfigId, True)
        leagues = get_summoner_league(region=region, summoner_id=summoner_id)
        for league in leagues:
            print(league['queueType'], ' something ', queue_type)

            if league['queueType'] == queue_type:
                wins = league['wins']
                losses = league['losses']
                win_percent = wins/(wins + losses)
                print('records')
                print(wins)
                print(losses)
                print(win_percent)

        record = "{win_percent} ({total} played)".format(win_percent=win_percent, total=total)

    except ValueError:
        return None
    return record

'''
CHAMP_NAMES = {  # For Data Dragon Lookup, Riots naming convention is inconsistent
    "Aatrox": "Aatrox",
    "Alistar": "Alistar",
    "Annie": "Annie",
    "Azir": "Azir",
    "Ahri": "Ahri",
    "Amumu": "Amumu",
    "Ashe": "Ashe",
    "Bard": "Bard",
    "Akali": "Akali",
    "Aurelion Sol": "AurelionSol",
    "Blitzcrank": "Blitzcrank",
    "Brand": "Brand",
    "Camille": "Camille",
    "Corki": "Corki",
    "Draven": "Draven",
    "Braum": "Braum",
    "Cassiopeia": "Cassiopeia",
    "Darius": "Darius",
    "Dr. Mundo": "DrMundo",
    "Caitlyn": "Caitlyn",
    "Cho'Gath": "Chogath",
    "Diana": "Diana",
    "Ekko": "Ekko",
    "Elise": "Elise",
    "Fiddlesticks": "Fiddlesticks",
    "Galio": "Galio",
    "Gnar": "Gnar",
    "Evelynn": "Evelynn",
    "Fiora": "Fiora",
    "Gangplank": "Gangplank",
    "Gragas": "Gragas",
    "Ezreal": "Ezreal",
    "Fizz": "Fizz",
    "Garen": "Garen",
    "Graves": "Graves",
    "Hecarim": "Hecarim",
    "Irelia": "Irelia",
    "Jarvan IV": "JarvanIV",
    "Jhin": "Jhin",
    "Heimerdinger": "Heimerdinger",
    "Ivern": "Ivern",
    "Jax": "Jax",
    "Jinx": "Jinx",
    "Illaoi": "Illaoi",
    "Janna": "Janna",
    "Jayce": "Jayce",
    "Kalista": "Kalista",
    "Karma": "Karma",
    "Katarina": "Katarina",
    "Kha'Zix": "Khazix",
    "Kog'Maw": "KogMaw",
    "Karthus": "Karthus",
    "Kayle": "Kayle",
    "Kindred": "Kindred",
    "LeBlanc": "Leblanc",
    "Kassadin": "Kassadin",
    "Kennen": "Kennen",
    "Kled": "Kled",
    "Lee Sin": "LeeSin",
    "Leona": "Leona",
    "Lulu": "Lulu",
    "Malzahar": "Malzahar",
    "Miss Fortune": "MissFortune",
    "Lissandra": "Lissandra",
    "Lux": "Lux",
    "Maokai": "Maokai",
    "Wukong": "MonkeyKing",
    "Lucian": "Lucian",
    "Malphite": "Malphite",
    "Master Yi": "MasterYi",
    "Mordekaiser": "Mordekaiser",
    "Morgana": "Morgana",
    "Nautilus": "Nautilus",
    "Nunu": "Nunu",
    "Pantheon": "Pantheon",
    "Nami": "Nami",
    "Nidalee": "Nidalee",
    "Olaf": "Olaf",
    "Poppy": "Poppy",
    "Nasus": "Nasus",
    "Nocturne": "Nocturne",
    "Oriana": "Oriana",
    "Quinn": "Quinn",
    "Rakan": "Rakan",
    "Renekton": "Renekton",
    "Rumble": "Rumble",
    "Shaco": "Shaco",
    "Rammus": "Rammus",
    "Rengar": "Rengar",
    "Ryze": "Ryze",
    "Shen": "Shen",
    "Rek'Sai": "RekSai",
    "Riven": "Riven",
    "Sejuani": "Sejauni",
    "Shyvanna": "Shyvanna",
    "Singed": "Singed",
    "Skarner": "Skarner",
    "Swain": "Swain",
    "Taliyah": "Taliyah",
    "Sion": "Sion",
    "Sona": "Sona",
    "Syndra": "Syndra",
    "Talon": "Talon",
    "Sivir": "Sivir",
    "Soraka": "Soraka",
    "Tahm Kench": "TahmKench",
    "Taric": "Taric",
    "Teemo": "Teemo",
    "Trundle": "Trundle",
    "Twitch": "Twitch",
    "Varus": "Varus",
    "Thresh": "Thresh",
    "Tryndamere": "Tryndamere",
    "Udyr": "Udyr",
    "Vayne": "Vayne",
    "Tristana": "Tristana",
    "Twisted Fate": "TwistedFate",
    "Urgot": "Urgot",
    "Veigar": "Veigar",
    "Vel'Koz": "Velkoz",
    "Vladimir": "Vladimir",
    "Xayah": "Xayah",
    "Yasuo": "Yasuo",
    "Vi": "Vi",
    "Volibear": "Volibear",
    "Xerath": "Xerath",
    "Yorick": "Yorick",
    "Viktor": "Viktor",
    "Warwick": "Warwick",
    "Xin Zhao": "XinZhao",
    "Zac": "Zac",
    "Zed": "Zed",
    "Zyra": "Zyra",
    "Ziggs": "Ziggs",
    "Zilean": "Zilean",
    "": ""
}
'''