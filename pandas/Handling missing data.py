
import pandas as pd
import numpy as np

data={
    'animal':['cat','dog','ele','snake','hen','huh'],
    'age':[2.5,3,np.nan,4,5,6],
    'visits':[1,3,2,3,3,2],
    'priority':['yes','yes','no','no','yes','no']
}
labels=['a','b','c','d','e','f']

df4=pd.DataFrame(data,index=labels)
print(df4)
df5=df4.copy()

#print(df4['age'].mean())
print(df4['age'].replace(np.NaN,df4['age'].mean()).tail())    #jesob jaygay nan value ache oigula age er mean value diye
                             #fill up kora & tail() er jonno last theke 5ta show kora

#df4.fillna(4)
#print(df4)


print(df5.isnull().sum())  # kotogulo data missing ta show kore

df5=df5.dropna(how='any')  # kono data empty thakle ta delete kore dey,,jemon NAN thaka mane empty
print(df5)











