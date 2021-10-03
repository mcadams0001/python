import pandas as pd
df = pd.read_csv('e:\\src\\python\\uni\\salesdata.csv', index_col='Month', usecols=['Month','Pens','Pencils'])
low_sales = df[(df.Pens<100) | (df.Pencils <100)]