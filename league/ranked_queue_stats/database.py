'''

import sqlite3

conn = sqlite3.connect('league_rank.db')
c = conn.cursor()


# create tables section
def create_table_summoner():
    c.execute("CREATE TABLE IF NOT EXISTS summoners(summonerId TEXT, accountId INTEGER, region TEXT)")


def create_table_matches():
    c.execute("CREATE TABLE IF NOT EXISTS matches(\
    accountId INTEGER, \
    platformId TEXT, \
    gameId INTEGER, \
    champion INTEGER, \
    queue TEXT, \
    season INTEGER, \
    timestamp INTEGER, \
    role TEXT, \
    lane TEXT, \
    win TEXT)")


def create_table_users():
    c.execute("CREATE TABLE IF NOT EXISTS users(\
    summonerName TEXT, \
    accountId INTEGER, \
    timestamp INTEGER)")


# read from the db section
def read_user_from_db(accountId):
    c.execute('SELECT accountId FROM users WHERE accountId=?', (accountId))
    data = c.fetchone()
    return data


def read_match_from_db(accountId, gameId):
    c.execute('SELECT gameId FROM matches WHERE accountId=? AND gameId=?', (accountId, gameId))
    data = c.fetchone()
    return data


def read_all_record(accountId):
    c.execute('SELECT * FROM matches WHERE accountId=?', (accountId,))
    data = c.fetchall()
    return data


def read_last_season_ranked_solo(accountId):
    c.execute('SELECT * FROM matches WHERE accountID=? AND queue=420 AND season=9', (accountId,))
    data = c.fetchall()
    return data


def read_2016_season_ranked_solo(accountId):
    c.execute('SELECT * FROM matches WHERE accountID=? AND queue=410 AND season=7', (accountId,))
    data = c.fetchall()
    return data


# add to the database
def add_match_information(accountId, platformId, gameId, champion, queue, season, timestamp, role, lane, win):
    c.execute("INSERT INTO matches(accountId, platformId, gameId, champion, queue, season, timestamp, role, lane, win) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (accountId, platformId, gameId, champion, queue, season, timestamp, role, lane, win))
    conn.commit()


def add_user_information(summonerName, accountId, timestamp):
    c.execute("INSERT INTO users(summonerName, accountId, timestamp) VALUES(?, ?, ?)",
              (summonerName, accountId, timestamp))
    conn.commit()
'''