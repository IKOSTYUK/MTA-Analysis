# Reading the .csv Files to Isolate Station Data

import glob
import pandas as pd

allFiles = glob.glob("*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)

station = frame.loc[frame['STATION'] == 'DEKALB AV']

station.to_csv('dekalb.csv', sep=',')

