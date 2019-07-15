#! C:\Anaconda3\envs\py3\python

import os
import time
import subprocess
from datetime import datetime


stoptime = datetime(2019, 7, 18, 20, 00, 0)

print(f'\n\nAuto-refresh will run until {str(stoptime)}\n\n')

while stoptime > datetime.now():
    print(datetime.now())
    subprocess.Popen(['C:\\Anaconda3\\envs\\py3\\python.exe', 'C:\\Stuff\\Programming\\golf_pool\\golf_leaderboard.py'])
    time.sleep(300)

print('''
    ********************************************
    ********************************************
    ************ Auto-refresh ended ************
    ********************************************
    ********************************************
    ''')
