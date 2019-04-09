#! C:/Anaconda/envs/py3/python

import requests, json, tournament_list

def generate_possible_ids():
	possible_ids = []
	for i in range(1000):
		possible_ids.append('0'*(3-len(str(i))) + str(i))
	return possible_ids
	

def get_tournament_list(id_list):
	tourney_list = []
	for id in id_list:
		res = requests.get('https://statdata.pgatour.com/r/{}/leaderboard-v2mini.json'.format(id))
		try:
			res.raise_for_status()
			data = json.loads(res.text)
			tourney_list.append([id, data['leaderboard']['tournament_name'], data['debug']['setup_year']])
		except requests.exceptions.HTTPError:
			print(id + 'Not a valid Tournamet ID')


	return tourney_list

possible_ids = generate_possible_ids()

# t_list = get_tournament_list(tournament_list.tlist_df['tid'])

print(get_tournament_list(tournament_list.tlist_df['tid'][:5]))
# if t_list == tournament_list.pga_id_list