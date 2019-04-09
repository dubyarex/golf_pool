#! C:/Anaconda/envs/py3/python

import requests, json, tournament_list

def generate_possible_ids():
	possible_ids = []
	# create a list of all possible 'tid' values [000-999]
	for i in range(1000):
		possible_ids.append('0'*(3-len(str(i))) + str(i))
	return possible_ids
	

def get_tournament_list(tid_list):
	### List generated on 2019-04-09 was printed and copied and pasted as a LoL
	### in tournament_list.py  May want to occasionally check for new 'tid's, or
	### check for Current Tournament 'tid' in tournament_list.py data and append
	### as needed.

	### Could start with headers and pop tourney_list[0] to create headers in a 
	### pandas DataFrame.  
	# tourney_list = [[list of column headers]]
	tourney_list = []
	### given a list of 'tid's -- check if URL exists and append tourney_list
	### 
	for id in tid_list:
		res = requests.get('https://statdata.pgatour.com/r/{}/leaderboard-v2mini.json'.format(id))
		### Check if URL exist
		try:
			res.raise_for_status()
			### create json object to query
			data = json.loads(res.text)
			### Create a list of ['tid', 'tname', 'tyear'] and append to tourney_list
			tourney_list.append([id, data['leaderboard']['tournament_name'], data['debug']['setup_year']])
		except requests.exceptions.HTTPError:
			### Show which 'tid's are not valid URLs
			print(id + 'Not a valid Tournamet ID')


	return tourney_list

possible_ids = generate_possible_ids()

# t_list = get_tournament_list(tournament_list.tlist_df['tid'])

