'''
Desc: mass convert xlsx to csv
Dest: ./csv/console.csv
Synt: py py_xlsx_to_csv_converter.py

Note: excel files should be in xlsx format
	  script should be placed inside xlsx directory

'''



import os
import sys
import pandas as pd
global dfc
dfc = pd.DataFrame()
dfc['a'] = ''

def export_csv(file):
	df = pd.read_excel(file)  
	print('converting: ' + file)
	# file = "consol.csv"
	cols = list(df.columns.values)
	cols.insert(0, 'file_name')
	df['file_name'] = file
	df = df[cols]
	file = "console.xlsx"
	df.to_csv('./csv/'  + file.replace(".xlsx", ".csv"),mode='a', header=True)
	# dfc = pd.concat([df,dfc], axis=0, ignore_index=1)

if not os.path.isdir('./csv'):
	os.mkdir('./csv', 0o666)

directory = './'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if filename.endswith('.xlsx'):
        	export_csv(filename)


# df1.join(df2.set_index('A'), on='A').dropna()



