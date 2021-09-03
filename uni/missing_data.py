#Strategies
#1. Ignore missing data
#2. Drop missing data
#3. Fill-in missing data

#In numpy missing data is NaN (Not a number)
# df.info() provides info on nun-null values for each column

import pandas as pd
import numpy as np
df = pd.read_csv('e:\\src\\python\\uni\\salesdata_missing.csv', index_col='Month')
df.info()
df.sum(axis=0)
df.mean(axis=0)
df.corr()

df = pd.read_csv('e:\\src\\python\\uni\\dropna.csv')
#drop data
df.dropna()
df['A'].dropna()
df.dropna(thresh=18)
df.dropna(axis=1, how='any')

#fill missing data
df.fillna(0.5)
df.fillna(df.mean())
df.T.fillna(df.mean(axis=1)).T

df = pd.read_csv('e:\\src\\python\\uni\\salesdata_blank.csv', index_col='Month')
df = df.replace(r'^\s*$', np.nan, regex=True)
df.isnull()
df.notnull()
df.isnull().sum() #total of missing values in each columns

df2 = df.fillna(df.interpolate(method='linear'))
df2