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
fig = plt.subplot(2,2,1)
x.plot()
plt.xlabel('Years')
plt.ylabel('Values')
plt.show()

