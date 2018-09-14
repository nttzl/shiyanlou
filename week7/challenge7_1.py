import pandas as pd


data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
df1 = pd.merge(data,country)

z = data.iloc[:,7:]
x = z.sum(axis=1)

df2 = df1[['Income group','Country name','Series code']]
df2['Sum emissions'] = x
df3 = df2[df2['Series code']='EN.ATM.CO2E.KT']
df4 = df3.groupby('Income group').sum()

