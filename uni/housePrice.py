import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
pd.options.display.float_format = '{:.2f}'.format
dfraw = pd.read_excel('e:/data/UK-HPI-full-file-2021-06.xlsx', sheet_name='UK-HPI-full-file-2021-06')

cols_to_include = ['Date','RegionName', 'DetachedPrice', 'SemiDetachedPrice','TerracedPrice','FlatPrice','OldSalesVolume']
dpricetype = dfraw[cols_to_include]
dfdist = pd.read_excel('e:/data/UK-HPI-full-file-2021-06.xlsx', sheet_name='Distance')
dprice2021 = dpricetype[(dpricetype['Date']>'01/01/2021')]
dprice2016 = dpricetype[(dpricetype['Date']>'01/01/2016') & (dpricetype['Date']<'01/01/2017')]
dmp2021=dprice2021.groupby('RegionName').mean()
dmp2016=dprice2016.groupby('RegionName').mean()

dmp2021.plot(figsize=(20,10))

sevenoaks = dpricetype[dpricetype.RegionName.eq('Sevenoaks')]
sevChange = sevenoaks[['Date','DetachedPrice', 'SemiDetachedPrice','TerracedPrice','FlatPrice']].groupby(dpricetype.Date.dt.year).mean().diff()
sevChange
sevChange.plot()

sevChange1621=sevChange.filter([2016,2017,2018,2019,2020,2021], axis=0)
sevChange1621
sevChange1621.plot()

dmp2021dist = dmp2021.merge(dfdist, right_on='RegionName', left_on='RegionName', how='outer')
dmp2016dist = dmp2016.merge(dfdist, right_on='RegionName', left_on='RegionName', how='outer')
dmp2021dist

detached2021 = dmp2021dist[['RegionName','DetachedPrice','OldSalesVolume','DistanceMiles']]
detached2021.corr()

detached2016 = dmp2016dist[['RegionName','DetachedPrice','OldSalesVolume','DistanceMiles']]
detached2016.corr()

plt.figure(figsize=(12,10))
ax = sns.heatmap(data=detached2021.corr(), annot=True, square=True)
ax.set_ylim(len(detached2021.corr()), -0.5)

plt.figure(figsize=(12,10))
ax = sns.heatmap(data=detached2016.corr(), annot=True, square=True)
ax.set_ylim(len(detached2016.corr()), -0.5)

dmp2021dist[['DetachedPrice','DistanceMiles']].plot()

proptype=dmp2021dist[['DetachedPrice','SemiDetachedPrice','TerracedPrice','FlatPrice']]
proptype.mean()