"""

import API
import database
import my_dicts
import pprint
import time
from operator import itemgetter

region = 'NA1'

# UPDATE THE RIOT API KEY!!! #

# implement numpy and pandas


def get_account_champs(data):
    champ_list = []
    for i in data:
        champ = i[3]
        if champ not in champ_list:
            champ_list.append(champ)
    return champ_list


def flatten_list(data):
    flat_data = []
    for sublist in data:
        for item in sublist:
            flat_data.append(item)
    return flat_data


def individual_champ_wr(data, champ):
    champ_stats = []
    for i in range(0, len(data), 1):
        if champ == data[i][3]:
            champ_stats.append(data[i])
    return champ_stats


def make_champ_wr_table(champ_list, data):
    champ_title = [["Champion", "Wins", "Losses", "WR", "Games"]]
    champ_table = []
    for i in range(0, len(champ_list), 1):
        individual_champ = individual_champ_wr(data, champ_list[i])
        flat_champ = flatten_list(individual_champ)
        if champ_list[i] in my_dicts.champs:
            champ = my_dicts.champs[champ_list[i]]
        else:
            champ = champ_list[i]
        overall_win = flat_champ.count('1')
        overall_loss = flat_champ.count('0')
        game_count = overall_win + overall_loss
        overall_WR = overall_win / (overall_win + overall_loss) * 100
        champ_stats = [champ, overall_win, overall_loss, str(int(overall_WR)) + "%", game_count]
        champ_table.append(champ_stats)
    champ_table.sort(reverse=True, key=(itemgetter(4)))
    champ_title.append(champ_table)
    return champ_title


def get_win(gameId, region, accountId):
    data = API.get_summoner_matchinfo(gameId, region)

    for i in data['participantIdentities']:
        cmd = i['player']['accountId']
        if cmd == accountId:
            participant_id = i['participantId']
            win = data['participants'][participant_id-1]['stats']['win']
    return win


def filter_season(data):
    print("Do you want to filter by season? (y/n)")
    filter_season = input("Do you want to filter by season? (y/n)")
    if filter_season == "y":
        filter_season_number = input("What season would you like to filter for? (1-7")
        for i in data:
            # somelist[:] = [tup for tup in somelist if determine(tup)]
            if i[5] != filter_season_number+2:
                data.pop(i)


def update_last_100_games(region, accountId):

    summonerMatchList = API.get_summoner_matchlist(region, accountId)
    print(summonerMatchList['matches'][0]['gameId'])
    database.create_table_matches()

    for i in range(summonerMatchList['startIndex'], summonerMatchList['endIndex'], 1):

        gameId = summonerMatchList['matches'][i]['gameId']
        match_check = database.read_match_from_db(accountId, gameId)

        if match_check is None:
            platformId = summonerMatchList['matches'][i]['platformId']
            champion = summonerMatchList['matches'][i]['champion']
            queue = summonerMatchList['matches'][i]['queue']
            season = summonerMatchList['matches'][i]['season']
            timestamp = summonerMatchList['matches'][i]['timestamp']
            role = summonerMatchList['matches'][i]['role']
            lane = summonerMatchList['matches'][i]['lane']
            win = get_win(gameId, region, accountId)

            database.add_match_information(accountId, platformId, gameId, champion, queue, season, timestamp, role,
                                           lane, win)


def grab_100_games(region, accountId, beginIndex):
    summonerMatchList = API.get_summoner_matchlist_index(region, accountId, beginIndex)
    print(summonerMatchList['matches'][0]['gameId'])
    database.create_table_matches()

    for i in range(0, len(summonerMatchList['matches']), 1):

        gameId = summonerMatchList['matches'][i]['gameId']
        match_check = database.read_match_from_db(accountId, gameId)

        if match_check is None:
            platformId = summonerMatchList['matches'][i]['platformId']
            champion = summonerMatchList['matches'][i]['champion']
            queue = summonerMatchList['matches'][i]['queue']
            season = summonerMatchList['matches'][i]['season']
            timestamp = summonerMatchList['matches'][i]['timestamp']
            role = summonerMatchList['matches'][i]['role']
            lane = summonerMatchList['matches'][i]['lane']
            win = get_win(gameId, region, accountId)

            database.add_match_information(accountId, platformId, gameId, champion, queue, season, timestamp, role,
                                           lane, win)


def update_all_user_games(region, accountId, beginIndex):
    summonerMatchList = API.get_summoner_matchlist_index(region, accountId, beginIndex)
    print(len(summonerMatchList['matches']))
    while len(summonerMatchList['matches']) == 100:
        grab_100_games(region, accountId, beginIndex)
        beginIndex += 100
        summonerMatchList = API.get_summoner_matchlist_index(region, accountId, beginIndex)
    grab_100_games(region, accountId, beginIndex)


def calculate_overall_winrate(accountId):
    data = database.read_all_record(accountId)
    flat_data = flatten_list(data)
    overall_win = flat_data.count('1')
    overall_loss = flat_data.count('0')
    overall_WR = overall_win / (overall_win + overall_loss) * 100
    print("Overall win rate: " + str(int(overall_WR)) + "%")
    # pprint.pprint(data)


def make_solo_ranked_table(accountId):
    data = database.read_last_season_ranked_solo(accountId)
    champ_list = get_account_champs(data)
    champ_table = make_champ_wr_table(champ_list, data)
    return champ_table


def make_2016_solo_ranked_table(accountId):
    data = database.read_2016_season_ranked_solo(accountId)
    champ_list = get_account_champs(data)
    champ_table = make_champ_wr_table(champ_list, data)
    return champ_table


def main():
    beginIndex = 0

    print("Hello summoner, we are currently only serving NA customers.")
    print("Please enter your summoner name:")
    summoner = input()
    database.create_table_users()

    # need to parse out the summoner id information from the json in the below line of code
    summonerInfo = API.get_summoner_info(summoner, region)
    accountId = summonerInfo['accountId']
    userCheck = database.read_all_record(accountId)

    if not userCheck:
        update_all_user_games(region, accountId, beginIndex)
        database.add_user_information(summoner, accountId, time.time())
    else:
        print("Would you like to update your records? (y/n)")
        update = input()
        if update == 'y':
            update_all_user_games(region, accountId, beginIndex)
            # database.update_user_information(time.gmtime(0))
        else:
            print("yo, no update")

    calculate_overall_winrate(accountId)
    data = database.read_all_record(accountId)
    champ_list = get_account_champs(data)
    champ_table = make_champ_wr_table(champ_list, data)
    pprint.pprint(champ_table)
    print("Last Season Solo/Duo Champ Win Rates")
    pprint.pprint(make_solo_ranked_table(accountId))
    print("Season 6 Solo/Duo Champ Win Rates")
    pprint.pprint(make_2016_solo_ranked_table(accountId))


main()
"""