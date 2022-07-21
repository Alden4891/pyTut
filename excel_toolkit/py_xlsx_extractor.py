
import sys
import os
import sys
import pandas as pd
from os.path import exists

global dfc
dfc = pd.DataFrame()
dfc['a'] = ''

if len(sys.argv) == 3:
	file = sys.argv[1]
	if exists(file):
		df = pd.read_excel(file)  
		# df = df[(df.origin == "JFK") & (df.carrier == "B6")]

		if sys.argv[2] in df.columns:
			uniq = df[sys.argv[2]].unique()
			if not os.path.isdir('./splitted'):
				os.mkdir('./splitted', 0o666)

			for criteria in uniq:
				# print(i)
				dfx = df[(df[sys.argv[2]] == criteria)]
				criteria = criteria.replace('/','')
				criteria = criteria.replace('  ',' ')
				filename = (file.replace('.xlsx','_') + criteria + '.xlsx').lower().replace(' ','_')
				dfx.to_excel('./splitted/'  + filename,header=True)
				print('+ ' + filename)
		else:
			print('Column doesn\'t exists!')
	else:
		print('File doesn\'t exists!')
else:
	print('Usage: py_xlsx_extractor <filename.xlsx> <column>')

