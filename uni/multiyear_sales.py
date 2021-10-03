import pandas as pd
import glob

from pandas.core.tools.numeric import to_numeric


def read_multifile_crime_data():
    crimeFiles = glob.glob('e:\\data\\crime\\2021-*-kent-street.csv')
    crimes = {}
    for filename in crimeFiles:
        stop = filename.find('-kent-street.csv')
        start = stop-2
        month = filename[start:stop]
        print(month)
        df = pd.read_csv(filename, index_col='Month')
        crimes[month]=df
    return crimes


crimes = read_multifile_crime_data()

print(crimes)

df = pd.concat(crimes, axis=0)

crimes['06']

def make_dataframe_from_sales_data(sales):
    #concatenate sales data as before
    df = pd.concat(sales,axis=0)
    # convert month strings to numbers
    lookup = {'Jan':'01','Feb':'02','Mar':'03',
              'Apr':'04','May':'05','Jun':'06',
              'Jul':'07','Aug':'08','Sep':'09',
              'Oct':'10','Nov':'11','Dec':'12'
              }
    df = df.rename(index=lookup)
    #convert the (year,month) to 'year-month' index
    df.index = ["-".join(x) for x in df.index.ravel()]
    # conver the year-month string to datetime object
    df.index = pd.to_datetime(df.index)
    return df

def plot_sales_data():
    df.plot()
    df.resample('Y').sum().plot()
