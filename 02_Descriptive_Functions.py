# In[1] - Documentation
"""
Script - 02_Descriptive_Functions.py
Decription - 
Author - Rana Pratap
Date - 2020
Version - 1.0
"""
print(__doc__)

# In[2] - Import and create dataframe
import pandas as pd
import numpy as np

d={'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper']),
'Age':pd.Series([25,26,25,23,30,29,23,34,40,30]),
'Rating':pd.Series([4.23,3.34,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80])}
df=pd.DataFrame(d)

print('-'*40)
print(df)

# In[3] - Base Functions
print('-'*40)
print('Sum: ',df.sum())
print('Mean: ',df.mean())
print('Standard Deviaition: ',df.std())
print('-'*40)

# In[4] - Description
print('Description: ')
df.describe()
print('-'*40)

# In[5] - Convert to Series
s=pd.Series()
print(s)
print('-'*40)

df = pd.DataFrame()
print(df)
# In[6]
del(d,df,s) 

# In[7]

def adder(ele1, ele2):
    return (ele1 + ele2)

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2) # Table wise function application

df.apply(np.mean) # Row-Column wise function application

df['col1'].map(lambda x:x*100) # Element wise Function application
print(df.apply(np.mean))

# In[]
del(df)
