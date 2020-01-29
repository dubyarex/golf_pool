#! C:\Anaconda3\envs\py3\python

import requests
import json
import sys
import os
import openpyxl
import get_picks
import time
import datetime
from pprint import pprint


def even_chop(l_data, total_splits):
    splits = []
    size = int(len(l_data) / total_splits)
    start = 0
    stop = size
    for n in range(total_splits):
        if n + 1 <= (len(l_data) % total_splits):
            stop += 1
        splits.append(l_data[start:stop])
        start = stop
        stop += size
    return splits


def remainder_chop(l_data, total_splits, nper_split):
    splits = []
    start = 0
    for n in range(total_splits):
        if n + 1 < total_splits:
            splits.append(l_data[start:(start + nper_split)])
            start += nper_split
        else:
            splits.append(l_data[start:])
    return splits


def get_tid():
    res = requests.get('https://statdata.pgatour.com/r/current/message.json')
    data = json.loads(res.text)
    tid = data['tid']
    return tid


def get_tournament(tid, year=None):
    if year:
        url = 'https://statdata.pgatour.com/r/{}/{}/leaderboard-v2mini.json'.format(tid, year)
    else:
        url = 'https://statdata.pgatour.com/r/{}/leaderboard-v2mini.json'.format(tid)
    res = requests.get(url)
    data = json.loads(res.text)
    t_name = data['leaderboard']['tournament_name']
    print(f'Getting Data for -- {t_name}')
    return data


def get_rankings():
    url = 'https://statdata.pgatour.com/r/stats/current/186.json'
    res = requests.get(url)
    rankings_data = json.loads(res.text)
    rank_date = rankings_data['tours'][0]['years'][0]['lastTrnProc']['endDate']
    rank_tournament = rankings_data['tours'][0]['years'][0]['lastTrnProc']['trnName']
    print("Rankings as of {} -- (Through {})".format(rank_date, rank_tournament))
    return rankings_data


def add_rankings(data):
    players_data = data['leaderboard']['players']
    rankings_data = get_rankings()
    rankings = rankings_data['tours'][0]['years'][0]['stats'][0]['details']
    playerlist = []
    for entry in players_data:
        first_initial = entry['player_bio']['short_name']
        last_name = entry['player_bio']['last_name']
        short_name = f'{first_initial}. {last_name}'
        entry['rankings']['cur_rank'] = 999
        for rank in rankings:
            if rank['plrNum'] == entry['player_id']:
                entry['rankings']['cur_rank'] = int(rank['curRank'])
        playerlist.append(entry)
    rankedlist = sorted(playerlist, key=lambda player: int(player['rankings']['cur_rank']))
    for player in rankedlist:
        if player['rankings']['cur_rank'] == 999:
            player['rankings']['cur_rank'] = None
    return rankedlist


def get_field(tid):
    url = 'https://statdata.pgatour.com/r/{}/field.json'.format(tid)
    res = requests.get(url)
    data = json.loads(res.text)
    print(f'Field for {data["Tournament"]["yyyy"]} -- {data["Tournament"]["TournamentName"]}')
    field = data["Tournament"]["Players"]
    player_list = []
    for player in field:
        details = {}
        details["player_id"] = player["TournamentPlayerId"]
        details["short_name"] = player["PlayerName"].split(',')[1][1]
        details["last_name"] = player["PlayerName"].split(',')[0]
        player_list.append(details)
    return player_list


def rank_field(data):
    rankings_data = get_rankings()
    rankings = rankings_data['tours'][0]['years'][0]['stats'][0]['details']
    player_list = []
    for player in data:
        player['rankings'] = {}
        player['rankings']['cur_rank'] = 999
        for rank in rankings:
            if rank['plrNum'] == player['player_id']:
                player['rankings']['cur_rank'] = int(rank['curRank'])
        player_list.append(player)
    ranked_list = sorted(player_list, key=lambda player: int(player['rankings']['cur_rank']))
    for player in ranked_list:
        if player['rankings']['cur_rank'] == 999:
            player['rankings']['cur_rank'] = None
    return ranked_list


# test = []
# for i in range(100):
#     test.append(i + 1)

# print(remainder_chop(test, 6, 10))


# wfg_id = get_tid()
# wfg_data = get_tournament(wfg_id)

# wfg_ranked = add_rankings(wfg_data)
# player_groups = remainder_chop(wfg_ranked, 6, 10)

# pprint(get_field("033"))

ranked_field = rank_field(get_field("003"))

# pprint(remainder_chop(ranked_field, 6, 10))
chopped = remainder_chop(ranked_field, 6, 10)

for split in enumerate(chopped, 1):
    print("Group {}".format(str(split[0])))
    for player in split[1]:
        print(f'{player["short_name"]}. {player["last_name"]}; {player["rankings"]["cur_rank"]}')


# pprint(wfg_data['leaderboard']['players'][0]['rankings'])
# pprint(wfg_ranked[1]['rankings'])
