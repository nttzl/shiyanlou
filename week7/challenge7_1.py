import pandas as pd
import numpy as np

def co2():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')

    data = data.drop(data.columns[0:5],axis=1)
#dfc = pd.merge(data,country)
    data = data.replace({'..':np.nan})
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    country = country.set_index('Country code')

    df = pd.concat([data.sum(axis=1),country[['Income group','Country name']]],axis=1)
    x = df.groupby('Income group').sum()
    x.columns = ['Sum emissions']

    y = df.sort_values(0,ascending=False).groupby('Income group').head(1).set_index('Income group')
    y.columns = ['Highest emissions','Highest emission country']

    z = df[df[0]>0].sort_values(0).groupby('Income group').head(1).set_index('Income group')
    z.columns = ['Lowest emissions','Lowest emission country']
    result = pd.concat([x,y,z],axis=1)
    return result       
#z=dfc.iloc[:,7:-4]
#z = z.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
#x = z.sum(axis=1)
#dfc['Sum emissions']=x

#df2 = dfc[['Income group','Country name','Sum emissions']]
#df2=df2.replace({0:np.nan})
#df2.dropna()
#df3 = df2.groupby('Income group').sum()
#df4 = df2.groupby('Income group').max()
#df5 = df2.groupby('Income group').min()

