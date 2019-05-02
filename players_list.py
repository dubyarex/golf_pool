#! C:\Anaconda3\envs\py3\python

import requests, json, sys, os, openpyxl, get_picks, time, datetime
from pprint import pprint

def even_chop(l_data, total_splits):
    splits = []
    size = int(len(l_data)/total_splits)
    start = 0
    stop = size
    for n in range(total_splits):
        if n+1 <= (len(l_data) % total_splits):
            stop += 1
        splits.append(l_data[start:stop])
        start = stop
        stop += size
    return splits

# def remainder_chop(l_data, total_splits, nper_split):
#     splits = []
#     strc_size = nper_split
#     start = 0
#     stop = strc_size
#     for n in range(total_splits):
#         if n+1 < total_splits:
#             splits.append(l_data[start:stop])
#         start = stop
#         stop += size
#     return splits

# pprint(structured_chop(test, 6, 5, 10))

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
    url = 'https://statdata.pgatour.com/r/stats/2019/186.json'
    res = requests.get(url)
    ranking_data = json.loads(res.text)
    return ranking_data


def get_players(data):
    players_data = data['leaderboard']['players']
    ranking_data = get_rankings()
    rankings = ranking_data['tours'][0]['years'][0]['stats'][0]['details']
    playerlist = []
    for entry in players_data:
        first_initial = entry['player_bio']['short_name']
        last_name = entry['player_bio']['last_name']
        short_name = f'{first_initial}. {last_name}'
        player_id = entry['player_id']
        player_info = {}
        player_info['player_id'] = player_id
        player_info['short_name'] = short_name
        player_info['cur_rank'] = 999
        for rank in rankings:
            if rank['plrNum'] == player_id:
                player_info['cur_rank'] = int(rank['curRank'])
        playerlist.append(player_info)
    rankedlist = sorted(playerlist, key = lambda player_info: int(player_info['cur_rank']))
    for i in rankedlist:
        if i['cur_rank'] == 999:
            i['cur_rank'] = None
    return rankedlist


# wfg_id = get_tid()
# wfg_data = get_tournament(wfg_id)


# print(wfg_data['leaderboard']['players'][0].keys())
# print(wfg_data['leaderboard']['players'][0]['player_bio'].keys())
# print(wfg_data['leaderboard']['players'][0]['rankings'].keys())
# pprint(get_players(wfg_data))
