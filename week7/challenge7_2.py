# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def co2_gdp_plot():

    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    co2 = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code').drop(data.columns[1:6],axis=1).replace({'..':pd.np.nan}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)
    gdp = data[data['Series code']=='NY.GDP.MKTP.CD'].set_index('Country code').drop(data.columns[1:6],axis=1).replace({'..':pd.np.nan}).fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)

    df = pd.concat([co2.sum(axis=1),gdp.sum(axis=1)],axis=1)
    df.columns = ['CO2-SUM','GDP-SUM']
    df = df.apply(lambda x:(x-x.min())/(x.max()-x.min()))  #这样比较优雅

#df2 = df.iloc[:,1:3].values
#df3 = df2/df2.max()
#df4 = pd.DataFrame(df3,columns=['CO2','GDP'])
#df4['Country code'] = country['Country code']
    fig = plt.subplot(1,1,1)       #1行1列第一个图
#plt.plot(df)
    df.plot(title='GDP-CO2',ax=fig)  #可以直接画出x轴刻度为index的图，如果用plt.plot(df),会报错string to float
#    plt.xlabel = 'Countries'
    plt.ylabel('Values')  #注意写法，不是‘=’
    plt.xlabel('Countries')

#plt.plot(df4.index,df4['CO2'])
#plt.plot(df4.index,df4['GDP'])
    plt.xticks((36,64,68,167,204),('CHN','FRA','GBR','RUS','USA'),rotation='vertical')
    plt.show()
    china = np.round(df[df.index=='CHN'].values,3).tolist()[0]  #四舍五入   [0]是因为结果要求是列表
#    china = np.round(df['CHN':'CHN'].values
    return fig,china

print(co2_gdp_plot())
