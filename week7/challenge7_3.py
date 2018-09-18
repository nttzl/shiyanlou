# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
df1 = data[data['Series code']=='EN.ATM.CO2E.KT']
df2 = data[data['Series code']=='EN.ATM.METH.KT.CE']
df3 = data[data['Series code']=='EN.ATM.NOXE.KT.CE']
df4 = data[data['Series code']=='EN.ATM.GHGO.KT.CE']
df5 = data[data['Series code']=='EN.CLC.GHGR.MT.CE']
df = pd.concat([df1,df2,df3,df4,df5]).iloc[:,6:-1].replace({'..':pd.np.nan}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
y = df.sum()
#df = df.apply(lambda x:(x-x.min())/(x.max()-x.min()))

temp = pd.read_excel('GlobalTemperature.xlsx')
temp = temp.set_index('Date')
temp = temp.drop(temp.columns[1:3],axis=1)
temp.index = pd.to_datetime(temp.index)
x = temp.resample('A').mean()['1990':'2010']
x.index = y.index
x['Total GHG'] = y
x = x.apply(lambda x:(x-x.min())/(x.max()-x.min()))
fig,axes = plt.subplots(2,2)
ax1 = x.plot(kind='line',figsize=(16,9),ax=axes[0,0],xticks=x.index)
ax1.set_xlabel('Years')
ax1.set_ylabel('Values')
ax2 = x.plot(kind='bar',figsize=(16,9),ax=axes[0,1])
ax2.set_xlabel('Years')
ax2.set_ylabel('Values')

z = temp.resample('Q').mean()
ax3 = z.plot(kind='area',figsize=(16,9),ax=axes[1,0])
ax4 = z.plot(kind='kde',figsize=(16,9),ax=axes[1,1])
