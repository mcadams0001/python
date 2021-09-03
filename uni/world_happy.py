import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.2f}'.format

dfraw = pd.read_excel('e:\Download\WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')

def produce_summary_table(df):
    column_renaming = {'count': 'N', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min.', 'max': 'Max.'}
    column_order = ['Mean', 'Std. Dev.', 'Min.', 'Max.', 'N']

    dfsummary = df.describe().T.drop(['year'],axis=0).drop(['25%','50%','75%'], axis=1).rename(column_renaming, axis=1)
    dfsummary = dfsummary[column_order]
    dfsummary['N'] = dfsummary['N'].astype(int)
    return dfsummary


dfsummary = produce_summary_table(dfraw)

