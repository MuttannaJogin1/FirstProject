# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:43:25 2023

@author: mjogin
"""
#%%
import pandas as pd
import numpy as np
import os
import datetime
os.chdir(r"C:\Users\mjogin\Desktop\Learnings\IKEA")

#%%
df=pd.read_excel("dwh_itm_csm_line_ev_t.xls")

check=df.columns

check1=df.dtypes

df['EVENT_DTIME_LOC']=pd.to_datetime(df.EVENT_DTIME_LOC,utc=True)
df['RESP_PARTY_REPORT_DTIME_LOC']=pd.to_datetime(df.RESP_PARTY_REPORT_DTIME_LOC,utc=True)

dob=df['RESP_PARTY_REPORT_DTIME_LOC']-df['EVENT_DTIME_LOC']

check1=df.dtypes

df['RESP_PARTY_REPORT_DTIME_LOC']=pd.to_datetime(df['RESP_PARTY_REPORT_DTIME_LOC'])

df.Date = pd.to_datetime(df.Date)
df.EVENT_DTIME_LOC = df.EVENT_DTIME_LOC.apply(lambda x: datetime.date(x.year, x.month, x.day))

df['day']=df['EVENT_DTIME_LOC'].dt.day



df['DOB1'] = df.EVENT_DTIME_LOC.dt.strftime('%m/%d/%Y')


df['ARR_ACT_DTIME_LOC']=pd.to_datetime(df.ARR_ACT_DTIME_LOC,utc=True)
df['UNL_ACT_DTIME_LOC']=pd.to_datetime(df.UNL_ACT_DTIME_LOC,utc=True)

df['ARR_ACT_DTIME_LOC1']=df['ARR_ACT_DTIME_LOC'].map(lambda x:str(x).split()[0])
df['UNL_ACT_DTIME_LOC1']=df['UNL_ACT_DTIME_LOC'].map(lambda x:str(x).split()[0])

df['ARR_ACT_DTIME_LOC1']=pd.to_datetime(df.ARR_ACT_DTIME_LOC1,utc=True)
df['UNL_ACT_DTIME_LOC1']=pd.to_datetime(df.UNL_ACT_DTIME_LOC1,utc=True)



df['unlarr']=df['UNL_ACT_DTIME_LOC1']-df['ARR_ACT_DTIME_LOC1']


anamoly=df['unlarr'].value_counts()

anamoly=anamoly.reset_index()

anamoly['dates']=anamoly['index'].dt.dates

anamoly['days']=anamoly['index'].map(lambda x:str(x).split()[0])


