import pandas as pd
import numpy as np

dates=pd.date_range('today',periods=6)  #dates & time sequence as index,,date started from today
#print(dates)
num_arr=np.random.randn(6,4)  # random numbers in 6 rows 4 columns
#print(num_arr)
columns=['A','B','C','D']  # as 4 columns

df1=pd.DataFrame(num_arr,index=dates,columns=columns)
print(df1)

#create dataframe with dictionary array
#index 0 thke shuru hoy

data={
    'animal':['cat','dog','ele','snake','hen','huh'],
    'age':[2.5,3,np.nan,4,5,6],
    'visits':[1,3,2,3,3,2],
    'priority':['yes','yes','no','no','yes','no']
}
labels=['a','b','c','d','e','f']

df2=pd.DataFrame(data,index=labels)
print(df2)
#print(df2.dtypes)  #data types

print(df2.head())  #head function prothom 5ta value show kore
#df3=df2.head(6)  #same as df2
print(df2.head(2)) #vitore number define kore dile totai dekhay 1st theke
print(df2.tail())  #tail function last 5ta value show kore
print(df2.tail(3))
print(df2.index)  #index show kore
print(df2.columns)  #column show kore
print(df2.values)  #values show kore
print(df2.describe())  #statistical info of data
print(df2.T)  #eta df2 ke transpose kore,mane columne ke row r row ke column kore

#sorting of data
print(df2.sort_values(by='age'))  #age onusare data sort kore
print(df2.sort_values(by='age')[1:3])  #age onusare data sort kore index 1 theke 2 er values show korbe

#slicing dataframe
print(df2[1:3])  # 1 theke 2 show korbe

#query dataframe by tag
print(df2[['age','visits']])  # age & visits column show korbe

print(df2.iloc[1:3])  # 1 & 2 no. row show korbe

#copy
df3=df2.copy()

print(df3.isnull())  #null value ache kina ta show kore

#specific position er value change
df3.loc['a','age']=22
print(df3)

#kono ekta column e mean value ber kora
print(df3[['age']].mean())
print(df3.mean())  #puro table er mean ber kora,,jara numerical tadertai dibe shudhu,,string auto bad porbe

#print(df3['visits'].min())
#print(df3['visits'].max())
print(df3['visits'].sum())

print(df3.sum())  #puro dataframe er sum

#string er upper lower
string=pd.Series(['a','aa','B','BB','AbC'])
print(string.str.lower())  #sob gulo letter choto hater kore
#print(string.str.upper())  #sob gulo letter boro hater kore


