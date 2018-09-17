import pandas as pd
import numpy as np

def co2():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    data = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')

    data = data.drop(data.columns[0:5],axis=1)   #把需要处理的数据单独拿出来，再后面fillna的时候才不会把不相关的数据填充
#dfc = pd.merge(data,country)  不用merge因为后面排序要把表分开，再用concat合并，用index来保证数据对齐比较好
    data = data.replace({'..':np.nan})  
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    country = country.set_index('Country code')

    df = pd.concat([data.sum(axis=1),country[['Income group','Country name']]],axis=1) #index一样，axis=1是横向
    x = df.groupby('Income group').sum()   #无法sum的数据会忽略，比如Country name
    x.columns = ['Sum emissions']

    y = df.sort_values(0,ascending=False).groupby('Income group').head(1).set_index('Income group') #0是竖向
    y.columns = ['Highest emissions','Highest emission country']

    z = df[df[0]>0].sort_values(0).groupby('Income group').head(1).set_index('Income group')
    z.columns = ['Lowest emissions','Lowest emission country']
    result = pd.concat([x,y,z],axis=1)
    return result       
#z=dfc.iloc[:,7:-4]
#z = z.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
#x = z.sum(axis=1)
#dfc['Sum emissions']=x  得出的结果比正确的要小一些，不知道为什么

#df2 = dfc[['Income group','Country name','Sum emissions']]
#df2=df2.replace({0:np.nan})    这种方法处理0的数据有点傻   不如df[df[0]>0]
#df2.dropna()
#df3 = df2.groupby('Income group').sum()
#df4 = df2.groupby('Income group').max()    max，min会把每列分别排序，把Country name按字母顺序排序，得出的结果不是一一对应的
#df5 = df2.groupby('Income group').min()

