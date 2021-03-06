#! C:/Anaconda/envs/py3/python

import pandas as pd

### results of running  get_tournament_list(id_list) from tournaments.py 
### on 2019-04-09 where id_list is list of the rannge of 000-999
### May want to occasionally check for new 'tid's, or check for Current 
### Tournament 'tid' in tournament_list.py data and append as needed
pga_tournament_list = [['002', 'Desert Classic', '2019'], 
	                   ['003', 'Waste Management Phoenix Open', '2019'], 
	                   ['004', 'Farmers Insurance Open', '2019'], 
	                   ['005', 'AT&T Pebble Beach Pro-Am', '2019'], 
	                   ['006', 'Sony Open in Hawaii', '2019'], 
	                   ['007', 'Genesis Open', '2019'], 
	                   ['009', 'Arnold Palmer Invitational presented by Mastercard', '2019'], 
	                   ['010', 'The Honda Classic', '2019'], 
	                   ['011', 'THE PLAYERS Championship', '2019'], 
	                   ['012', 'RBC Heritage', '2018'], 
	                   ['013', 'Wyndham Championship', '2018'], 
	                   ['014', 'The Masters', '2018'], 
	                   ['016', 'Sentry Tournament of Champions', '2019'], 
	                   ['018', 'Zurich Classic of New Orleans', '2018'], 
	                   ['019', 'AT&T Byron Nelson', '2018'], 
	                   ['020', 'Houston Open', '2018'], 
	                   ['021', 'Fort Worth Invitational', '2018'], 
	                   ['023', 'the Memorial Tournament presented by Nationwide', '2018'], 
	                   ['025', 'FedEx St. Jude Classic', '2018'], 
	                   ['026', 'U.S. Open', '2018'], 
	                   ['027', 'THE NORTHERN TRUST', '2018'], 
	                   ['028', 'BMW Championship', '2018'], 
	                   ['030', 'John Deere Classic', '2018'], 
	                   ['032', 'RBC Canadian Open', '2018'], 
	                   ['033', 'PGA Championship', '2018'], 
	                   ['034', 'Travelers Championship', '2018'], 
	                   ['041', 'Valero Texas Open', '2019'], 
	                   ['047', 'Shriners Hospitals for Children Open', '2019'], 
	                   ['054', 'Sanderson Farms Championship', '2019'], 
	                   ['058', 'QBE Shootout', '2019'], 
	                   ['060', 'TOUR Championship', '2018'], 
	                   ['100', 'The Open Championship', '2018'], 
	                   ['169', 'ISPS HANDA World Cup of Golf', '2019'], 
	                   ['457', 'Mayakoba Golf Classic', '2019'], 
	                   ['464', 'Safeway Open', '2019'], 
	                   ['471', 'Quicken Loans National', '2018'], 
	                   ['472', 'Barracuda Championship', '2018'], 
	                   ['473', 'World Golf Championships-Mexico Championship', '2019'], 
	                   ['475', 'Valspar Championship', '2019'], 
	                   ['476', 'World Golf Championships-Bridgestone Invitational', '2018'], 
	                   ['478', 'Hero World Challenge', '2019'], 
	                   ['480', 'Wells Fargo Championship', '2018'], 
	                   ['483', 'Puerto Rico Open', '2019'], 
	                   ['489', 'World Golf Championships-HSBC Champions', '2019'], 
	                   ['490', 'A Military Tribute at The Greenbrier', '2018'], 
	                   ['493', 'The RSM Classic', '2019'], 
	                   ['494', 'CIMB Classic', '2019'], 
	                   ['500', 'Presidents Cup', '2017'], 
	                   ['505', 'Dell Technologies Championship', '2018'], 
	                   ['518', 'Barbasol Championship', '2018'], 
	                   ['519', "Olympic Men's Golf Competition", '2016'], 
	                   ['521', 'The CJ CUP', '2019'], 
	                   ['522', 'Corales Puntacana Resort & Club Championship', '2019'], 
	                   ['526', 'Tiger vs. Phil', '2019'], 
	                   ['650', "Olympic Women's Golf Competition", '2016']]

### transform list of list into a pandas DataFrame
### Default numeric indexing
# gittlist_df = pd.DataFrame(pga_tournament_list, columns=['tid', 'tname', 'tyear'])

### Use below to Index by 'tid'
tlist_df = pd.DataFrame(pga_tournament_list, columns=['tid', 'tname', 'tyear']).set_index('tid')
tlist_df.to_csv('list_of_tournaments.csv')


##### examples of how to accest data in the tlist_df DataFrame #####

### Returns 'tname' for given 'tid' <'014'>
# print(tlist_df.loc['014', 'tname'])
# print(tlist_df.at['014', 'tname'])

### Return 'tid' given 'tname' value <'The Master'>
# for d in tlist_df.index:
# 	if tlist_df.at[d , 'tname'] == 'The Masters':
# 		print(d)

### Return row(s) given 'tname' value <'The Master'>
# print(tlist_df.loc[tlist_df['tname'] == 'The Masters'])