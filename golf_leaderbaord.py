#! C:\Anaconda3\envs\py3\python

import requests, json, sys, os, openpyxl
from pprint import pprint
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.styles import Alignment, Font, Protection

### Have user choose which tournament to update
# tournament_name = input('Enter Desired Tournament: ')

### Placeholder while testing code
tid = '014'  # The Masters  'tid' for PGA.com
# PGA.com URL given a tournament ID - 'tid'
url = 'https://statdata.pgatour.com/r/{}/leaderboard-v2mini.json'.format(tid)
res = requests.get(url)

### parses json code into python data format (Dictionaries and Lists)
data = json.loads(res.text)

leaderboard = data['leaderboard']
### List of Desired tournament detail fields
# print(leaderboard.key())  # To see all possible fields


leaderboard_headers = ['tournament_id', 'tournament_name', 'stat_date', 'end_date', 'is_stated', 'is_finished', 'current_round', 'round_state']
# leaderboard['courses'][0]
course_sub_headers = ['course_id', 'course_name', 'par_in', 'par_out', 'par_total']
# leaderboard['cut_line']
cutline_sub_headers = ['cut_count', 'cut_line_score']
tournament_headers = leaderboard_headers + course_sub_headers + cutline_sub_headers
pprint(tournament_headers)
tournament_details = {}





'''
### Get Dictionary for Desired Tournament
for leaderboard in data['Leaderboards']:
	if leaderboard['Tournament'] == tournament_name:
		tournament_data = leaderboard

player_data = tournament_data['Players']

player_list = []
for player in player_data:
	player_list.append(player['Name'])

player_count = len(player_list)
column_titles = ['Name', 'Short Name', 'CurrentPosition', 'Total', 'After', 'Today', 'Round 1', 'Round 2', 'Round 3', 'Round 4', 'TotalStrokes']
col_count = len(column_titles)


### Check for existing file and open or create new file
if os.path.isfile('leader_test_2019.xlsx'):
	wb = openpyxl.load_workbook('leader_test_2019.xlsx')
### Create a new excel file
else:
	wb = openpyxl.Workbook()
	sheet = wb.active
	sheet.title = 'Raw Data'

### Select Raw Data Sheet
sheet = wb['Raw Data']

### Creating Title for Data Table
# sheet.merge_cells('A1:' + get_column_letter(col_count) + '1')
sheet['A1'] = tournament_name
sheet['A1'].font = Font(size=24, bold=True, underline="single")
sheet['A1'].alignment = Alignment(horizontal='center', vertical='center')

### Adds Columns Titles to Data Table
for i in range(1, len(column_titles) + 1):
	sheet.cell(row=2, column=i).value = column_titles[i-1]
	sheet.cell(row=2, column=i).font = Font(bold=True)

### Function to Generate Short Names
def shorten_name(full_name):
	names = full_name.split()
	name_count = len(names)
	short_name = names[0][0] + '. ' + ' '.join(names[1:])
	return(short_name)

### Add Short_Names and separate Round Scores
for player in player_data:
	player['Short Name'] = shorten_name(player['Name'])
	for round_num in list(enumerate(['Round 1', 'Round 2', 'Round 3', 'Round 4'])):
		player[round_num[1]] = player['Rounds'][round_num[0]]

### Iterate through players and write data to excel sheet
row_num = 3
for player in player_data:
	col_num = 1
	for col in column_titles:
		sheet.cell(row=row_num, column=col_num).value = player[col]
		col_num += 1
	row_num += 1



# col_num = 1
# for col in parser.keys():               # Iterate thorugh each Column
# 	for player in range(player_count):
# 		if col_num > 2:
# 			if leaderboard.select(parser[col])[player].getText() == 'E':
# 				sheet.cell(row=player+3, column=col_num).value = 0
# 			elif leaderboard.select(parser[col])[player].getText() == '-' or leaderboard.select(parser[col])[player].getText() == '--':
# 				sheet.cell(row=player+3, column=col_num).value = 'Cut'
# 			else:
# 				sheet.cell(row=player+3, column=col_num).value = int(leaderboard.select(parser[col])[player].getText())  # Iterate through each row in a Column 
# 		else:
# 			sheet.cell(row=player+3, column=col_num).value = leaderboard.select(parser[col])[player].getText()
# 	col_num += 1


sheet.column_dimensions['A'].width = 20
sheet.column_dimensions['B'].width = 20

wb.save('leader_test_2019.xlsx')

pprint(player_data[70])
'''