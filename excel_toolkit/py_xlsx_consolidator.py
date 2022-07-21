'''
Desc: excel merger
Dest: ./consolidated.xlsx
Synt: py py_xlsx_to_csv_converter.py

Note: excel files should be in xlsx format
	  script should be placed inside xlsx directory

pip install pyxlsb
pip install pandas
pip install pandas --upgrade
pip install openpyxl


'''

import os
import sys
import pandas as pd
global dfc
dfc = pd.DataFrame()
dfc['a'] = ''

directory = './'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if filename.endswith('.xlsx'):
            if not "consolidate" in filename:
            	print('file: ' + filename)
            	dfx = pd.read_excel(filename)
            	cols = list(dfx.columns.values)
            	cols.insert(0, 'source_filename')
            	dfx['source_filename'] = filename  
            	dfc = pd.concat([dfx,dfc], axis=0, ignore_index=1)
print('Saving result...')
dfc.to_excel("consolidated.xlsx")
print('All done!')
# df1.join(df2.set_index('A'), on='A').dropna()



