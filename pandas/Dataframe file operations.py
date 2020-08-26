
import pandas as pd
import numpy as np
import xlrd

data={
    'animal':['cat','dog','ele','snake','hen','huh'],
    'age':[2.5,3,np.nan,4,5,6],
    'visits':[1,3,2,3,3,2],
    'priority':['yes','yes','no','no','yes','no']
}
labels=['a','b','c','d','e','f']

df4=pd.DataFrame(data,index=labels)
print(df4)
df3=df4.copy()
#csv file
df4.to_csv('animal.csv')  #saved animal to harddrive  #df_animal er sob info animal.csv te jabe
df_animal=pd.read_csv('animal.csv')  #df_animal e animal.csv read kora
print(df_animal)
print(df_animal.head(4))
#print(df_animal.tail())

#xlsx file
df4.to_excel('animal.xlsx',sheet_name='Sheet1')  #saved animal to harddrive  #df_animal er sob info animal.xlsx te jabe
df_animal=pd.read_excel("animal.xlsx",'Sheet1',index_col=None,na_values=['NA']) #df_animal e animal.xlsx read kora
print(df_animal)


