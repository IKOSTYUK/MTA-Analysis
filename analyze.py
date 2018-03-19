#Analyzing Station Data

%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#load data and parse data column as datetime
df = pd.read_csv('dekalb.csv', parse_dates=[7])

#adding a month and year column for analysis
df['year'], df['month'] = df['DATE'].dt.year, df['DATE'].dt.month

#filtering only specific rows based on the below criteria for cleaner data
df1 = df[(df.LINENAME == 'BDNQR') & (df.DESC == 'REGULAR') & (df.year >= 2016) & (df.year <= 2017)]

#Grouping cummalitve entries by date
df1 = df1.groupby( [ "DATE", "TIME", 'year', 'month'], as_index=False )[["ENTRIES"]].sum()

#Calculating difference in daily cummulative entries to find actual number of entry per day (delta)
df1['delta'] = df1['ENTRIES'] - df1['ENTRIES'].shift(1)

#Grouping delta  by day
df2 = df1.groupby( ["DATE", 'year', 'month'], as_index=False )[["delta"]].sum()

#Getting rid of outliers
df3 = df2[(df2.delta >= 0) & (df2.delta <= 40000)]

#Plot and analyze

df3pivot = pd.pivot_table(df3,index=["month"],values=["delta"],
               columns=["year"],aggfunc=[np.sum])
print(df3pivot)

df3pivot.plot(kind = 'bar')

