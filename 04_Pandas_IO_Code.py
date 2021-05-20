# In[1] - Documentation
"""
Script -04_Pandas_IO_Code.py
Decription - 
Author - Rana Pratap
Date - 2020
Version - 1.0
"""
print(__doc__)

# In[2] - Import and Create data frame from names.csv
import pandas as pd
import numpy as np

df = pd.read_csv('names.csv',
    index_col=['SlNo'],             # Specify the Index row number
    dtype={'Salary':np.float64}     # Type Cast Salary column
    #,names=['A','B','C','D','E']   # Specify names for columns
    )
print(df)
print(df.dtypes)

# In[3] - Create data frame from names.csv
df1 = pd.read_csv('names.csv',skiprows=2)   # Skip the number of rows specified
print(df1)

# In[4]
del(df,df1)
