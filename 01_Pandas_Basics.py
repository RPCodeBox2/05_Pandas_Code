# In[1] - Documentation
"""
Script - 01_Pandas_Basics.py.py
Decription - Basic functional of Pandas
Author - Rana Pratap
Date - 2020
Version - 1.0
"""
print(__doc__)

# In[2] - Import and Create data frames
import pandas as pd

## Create DataFrame by Column (Top - Down)
df = pd.DataFrame(
    {'a':[4,5,6],
    'b':[7,8,9],
    'c':[10,11,12]},
    index = [1,2,3])
print(df)
print('-'*40)

## Create DataFranme by Rows (Side ways)
df = pd.DataFrame(
    [[4,7,10],
    [5,8,11],
    [6,9,12]],
    index=[1,2,3],
    columns=['a','b','c'])
print(df)
print('-'*40)

# In[3] - Create DataFrame with a MultiIndex
df1 = pd.DataFrame(
    {"a" : [4 ,5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]},
    index = pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2)],names=['n','v']))
print(df1)
print('-'*40)

df2 = (pd.melt(df)
    .rename(columns={'variable' : 'var ',
        'value' : 'val'})
    .query('val >= 200'))
print(df2)
print('-'*40)

# In[4] - Reshaping Data - Change the layout of a data set
## Gather columns into 1 row Melt.
print('Gather columns into rows\n')
df1 = pd.melt(df)
print(df1)

## Spread rows into columns - Pivot.
print('Spread rows into columns - Pivot')
df2 = df.pivot(columns='var',values='val')
print(df2)

## Append rows of DataFrames
pd.concat([df1,df2])
## Append columns of DataFrames
pd.concat([df1,df2], axis=1)

# In[5] - Order rows by values of a column (low to high).
df.sort_values('mpg')

# Order rows by values of a column (high to low).
df.sort_values(mpg',ascending =False)

# Rename the columns of a DataFrame
df.rename(columns = {y':'year'})

# Sort the index of a DataFrame
df.sort_index()

# Reset index of DataFrame to row numbers, moving index to columns.
df.reset_index()

# Drop columns from DataFrame
df.drop(columns=['Length','Height'])

# In[6] - Subset Observations - Rows
## Extract rows that meet logical criteria
df[df.Length > 7]

## Remove duplicate rows (only considers columns).
df.drop_duplicates

## Select first n rows.
df.head(n)

## Select last n rows.
df.tail(n)

## Randomly select fraction of rows.
df.sample(frac=0.5)

## Randomly select n rows.
df.sample(n)

## Select rows by position.
df.iloc[10:20]

## Select and order top n entries.
df.nlargest(n,'value')

## Select and order bottom n entries.
df.nsmallest(n, 'value')

# In[7] - Subset Variables (Columns)
## Select multiple columns with specific names
df[[width','length','species]]

## Select single column with specific name
df['width'] or df.width

## Select columns whose name matches regular expression regex
df.filter(regex='regex')

## Select all columns between x2 and x4 (inclusive)
df.loc[:,'x2':'x4']

## Select columns in positions 1, 2 and 5 (first column is 0)
df.iloc[:,[1,2,5]]

## Select rows meeting logical condition, and only the specific columns
df.loc[df ['a'] > 10, ['a','c']]

# In[8] - Summarize Data

## Count number of rows with each unique value of variable
df['w'].value_counts()

# of rows in DataFrame
len(df)

## of distinct values in a column.
df['w'].nunique()

## of distinct values in a column.
df.iloc[:,:],[index.unique]

## Basic descriptive statistics for each column (or GroupBy)
df.describe()

## Sum values of each object
sum()

##Count non NA/null values of each object
count()

## Median value of each object.
median()

## Quantiles of each object.
quantile([0.25,0.75])

## Apply function to each object.
apply(function)

## Minimum value in each object.
min()

## Maximum value in each object.
max()

## Mean value of each object.
mean()

## Variance of each object.
var()

## Standard deviation of each object.
std()

# In[9] - Handling Missing Data

## Drop rows with any column having NA/null data.
df.dropna()

## Replace all NA/null data with value.
df.fillna(value)

# In[10] - Make New Columns

## Compute and append one or more new columns.
df.assign(Area=lambda df: df.Length df.Height)

## Add single column.
df['Volume'] = df.Length df.Height df.Depth

## Bin column into n buckets.
pd.qcut(df.col , n, labels=False)

## Element wise max
max(axis=1)

## Element wise min
min(axis=1)

## Trim values at input thresholds
clip(lower=-10,upper=10)

## Absolute value
abs()

# In[11] - Group Data

## Return a GroupBy object, grouped by values in column named "col".
df.groupby(by="col")

## Return a GroupBy object, grouped by values in index level named "ind"
df.groupby(level='ind')

## Size of each group
size()

## Aggregate group using function
agg(function)

## Copy with values shifted by 1
shift(1)

##Copy with values lagged by 1.
shift(-1)

## Ranks with no gaps
rank(method='dense')

## Ranks. Ties get min rank
rank(method='min')

## Ranks rescaled to interval [0, 1].
rank(pct=True)

## Ranks. Ties go to first value.
rank(method='first')

## Cumulative sum
cumsum()

## Cumulative max
cummax()

## Cumulative min
cummin()

## Cumulative product
cumprod()

# In[12] - Windows

## Return an Expanding object allowing summary functions to be applied cumulatively.
df.expanding()

## Return a Rolling object allowing summary functions to be applied to windows of length n.
df.rolling(n)


# In[13] - Plotting

## Histogram for each column
df.plot.hist()

## Scatter chart using pairs of points
df.plot.scatter(x='w',y ='h')

# In[14] - Combine Data Sets

## Join matching rows from bdf to adf
pd.merge(adf , bdf, how='left', on='x1')

## Join matching rows from adf to bdf
pd.merge(adf, bdf, how='right', on='x1')

## Join data. Retain only rows in both sets.
pd.merge(adf, bdf, how='inner', on='x1')

## Join data. Retain all values, all rows.
pd.merge(adf, bdf, how='outer', on='x1')

## All rows in adf that have a match in bdf
adf[adf.x1.isin(bdf.x1)]
 
## All rows in adf that do not have a match in bdf
adf[~adf.x1.isin(bdf.x1)]

## Rows that appear in both ydf and zdf (Intersection)
pd.merge(ydf, zdf)

## Rows that appear in either or both ydf and zdf (Union)
pd.merge(ydf, zdf, how='outer')

## Rows that appear in ydf but not zdf (Setdiff)
pd.merge(ydf, zdf, how='outer',indicator=True)
    .query('_merge == "left_only"')
    .drop(columns=['_merge'])
#====================================================================

#====================================================================
#====================================================================
#====================================================================


