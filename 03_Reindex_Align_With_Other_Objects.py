# In[1] - Documentation
"""
Script - 03_Reindex_Align_With_Other_Objects.py
Decription - Pandas code for reindex a dataframe
Author - Rana Pratap
Date - 2020
Version - 1.0
"""
print(__doc__)

# In[2] - Import and Create data frame
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

# In[3] - Reindex Index

#Reindex to match new set of labels
df1 = df1.reindex_like(index=[0,2,5],column=['A','C','B'])
print(df1)

#Reindex in align to other objects
df1 = df1.reindex_like(df2)
print(df1)

df2 = df2.reindex_like(df1)
print(df2)

#forward fill method specified
df2 = df2.reindex_like(df1,method='ffill',limit=1)
print(df2)

#Rename
df1 = df1.rename(columns={'col1':'c1','col2':'c2'},index={1:'apple',1:'banana',2:'durian'})
print(df1)

# In[]
del(df1,df2)
