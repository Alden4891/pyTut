from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import A4 
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import registerFont	
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import math
import pandas as pd
import numpy as np
import io
	
#https://www.reportlab.com/snippets/30/

df = pd.read_excel("ID.xlsx","Sheet1")  
df_addr = df[['PROVINCE','CITY/MUNICIPALITY','BARANGAY']].drop_duplicates()
img = ImageReader('./images/id.jpg')
registerFont(TTFont('arial-narrow-bold','C:\\windows\\fonts\\ARIALNB.TTF'))
print('Initializing...')

def add_page(df,page):
	
	index = ((page-1)*10)

	dfx = df.iloc[index:index+10]
	dfx = dfx.sort_values(['FULL NAME'], ascending = [True])

	scale = .269
	x = 54
	y = 10
	w = 242
	h = 153

	for i in range(0,5):
		dfxx  =  dfx.iloc[i*2:i*2+2]
		dfxx = dfxx.reset_index()
		canvas.setFillColor((0,0,0)) 

		# COLUMN 1
		if len(dfxx.index) == 0:
			break
	
		hhid1 = dfxx._get_value(0,'HOUSEHOLD ID')
		prov1 = dfxx._get_value(0,'PROVINCE')
		muni1 = dfxx._get_value(0,'CITY/MUNICIPALITY')
		brgy1 = dfxx._get_value(0,'BARANGAY')
		fn1 = dfxx._get_value(0,'FULL NAME')

		canvas.drawImage(img,x,    668-156*i,w,h,anchor='sw',anchorAtXY=True,showBoundary=False)
		canvas.setFont('arial-narrow-bold',8)
		canvas.drawCentredString(x+185,668+65-156*i,fn1)
		canvas.drawCentredString(x+185,668+55-156*i,hhid1)
		canvas.setFont('arial-narrow-bold',7)
		canvas.drawCentredString(x+185,668+45-156*i,brgy1+', '+muni1)
		canvas.setFont('arial-narrow-bold',8)
		canvas.drawCentredString(x+185,668+35-156*i,prov1)

		# COLUMN 2
		if len(dfxx.index) == 1:
			break
		muni2 = dfxx._get_value(1,'CITY/MUNICIPALITY')
		hhid2 = dfxx._get_value(1,'HOUSEHOLD ID')
		prov2 = dfxx._get_value(1,'PROVINCE')
		brgy2 = dfxx._get_value(1,'BARANGAY')
		fn2 = dfxx._get_value(1,'FULL NAME')

		canvas.setFont('arial-narrow-bold',8)
		canvas.drawImage(img,x+247,668-156*i,w,h,anchor='sw',anchorAtXY=True,showBoundary=False)
		canvas.drawCentredString(x+185+247,668+65-156*i,fn2)
		canvas.drawCentredString(x+185+247,668+55-156*i,hhid2)
		canvas.setFont('arial-narrow-bold',7)
		canvas.drawCentredString(x+185+247,668+45-156*i,brgy2+', '+muni2)
		canvas.setFont('arial-narrow-bold',8)
		canvas.drawCentredString(x+185+247,668+35-156*i,prov2)
		
	canvas.drawCentredString(x+185+247+35,20,'Page '+ str(page))
	canvas.drawCentredString(x+210+30,668+100+50+10,prov1+', '+muni1+', '+brgy1)
	canvas.drawString(x,30,'Department of Social Welfare and Development Field Office XII')
	canvas.drawString(x,20,'Pantawid Pamilyang Pilipino Program')
	canvas.showPage()

for p,m,b in df_addr.values:
	print(p,m,b,' - success')
	buffer = io.BytesIO()
	canvas = Canvas(("./release/Pantawid_id_"+p+'_'+m+'_'+b+".pdf").replace(' ','_').replace("'","").replace("\\","").lower(), pagesize=A4,encrypt="dswd@123")
	canvas.setTitle("DSWD-PANTAWID ID")
	df_b = df.query('`CITY/MUNICIPALITY`=="' + m + '" & `BARANGAY`=="' + b + '" ')
	for i in range(1,math.ceil(len(df_b.index)/10)+1):
		add_page(df_b,i)
	canvas.save()
print('Done!')