import pandas as pd
import numpy as np

def co2():

    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    df1=pd.merge(data,country)
    dfc = df1[df1['Series code']=='EN.ATM.CO2E.KT']
    dfc = dfc.replace({'..':np.nan})
    dfc = dfc.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    z=dfc.iloc[:,7:-4]
    x = z.sum(axis=1)
    dfc['Sum emissions']=x
    df2 = dfc[['Income group','Country name','Sum emissions']]
    df2=df2.replace({0:np.nan})
    df2.dropna()
    df3 = df2.groupby('Income group').sum()
    df4 = df2.groupby('Income group').max()
    df5 = df2.groupby('Income group').min()
    df3['Highest emission country'] = df4['Country name']
    df3['Highest emissions'] = df4['Sum emissions']
    df3['Lowest emission country'] = df5['Country name']
    df3['Lowest emissions'] = df5['Sum emissions']
    return df3

if __name__ == '__main__':
    print(co2())
