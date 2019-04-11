#! C:\Anaconda3\envs\py3\python

import os, csv
import pandas as pd
from pprint import pprint

def from_excel(filepath):
	return pd.read_excel(filepath, header=0, index_col=0, usecols='A:G')

def from_csv(filepath):
	with open(filepath, newline='') as csvfile:
		return list(csv.reader(csvfile))