
import pandas as pd
import numpy as np

#datafram
#dictionary

df=pd.DataFrame({
    'A':[1,2,3,4],
    'B':pd.Timestamp('20200301'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([5]*4,dtype='int32'),
    'E':pd.Categorical(['true','false','true','false']),
    'F':'hello'

})

print(df)
#print(df.dtypes)  #kar kon data type
#print(df.head)
#print(df.tail)
print(df.index)
print(df.columns)
#print(df.to_numpy())
print(df.describe())
#print(df.sort_index(axis=1,ascending=False))
print(df.sort_values(by='C'))
print(df['C'])  #C column er value print
print(df[0:3])  # 0-2 porjonto row er value
#print(df.loc[D[0]])

#multi access by label
print(df.loc[:,['A','C']])
#print(df.loc['20200301':'20200302',['A','C']])  #data empty na hole 2020-03-01 theke 2020-03-02 porjonto
#data show kore
#print(df.loc['20200302',['A','C']])
#print(df.at[d[0],'C'])  # exact ekta vaue pawar jonno

#select a value inside a dataframe
print(df.iloc[3])  #ekta positioner sob value
#print(df.loc[2:3])  # 2-3 pos er sob value print
print(df.iloc[1:3])  # 1 theke 2 er sob value
print(df.iloc[1:3,2:4]) # 1thke 2 er 2 theke 3 er value print

print(df[df['A']>1])  # A er jesob man 0 theke boro oigula print









